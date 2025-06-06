import streamlit as st
from hf_utils import query_hf_model
from reasoning_checker import check_math_step, check_logic_step
from prompts import THINKER_PROMPT, CRITIC_PROMPT

st.set_page_config(page_title="🧠 CoT Verifier", layout="wide")
st.title("🔍 Chain-of-Thought Verifier with Proof Tracing")

hf_token = st.text_input("Hugging Face Token", type="password", help="https://huggingface.co/settings/tokens")
question = st.text_area("Enter a question:", height=100, placeholder="E.g., Solve x² + 5x + 6 = 0")

if st.button("Verify"):
    if not hf_token or not question.strip():
        st.warning("Enter both token and a valid question.")
    else:
        with st.spinner("Thinking..."):
            reasoning = query_hf_model(THINKER_PROMPT.format(question=question), hf_token)

        st.markdown("---")
        st.subheader("🧾 Full Reasoning Chain")
        st.code(reasoning)

        with st.spinner("Extracting Claims..."):
            claims_raw = query_hf_model(CRITIC_PROMPT.format(reasoning=reasoning), hf_token)

        st.markdown("---")
        st.subheader("🔍 Extracted Claims")
        st.text(claims_raw)

        st.markdown("---")
        st.subheader("✅ Verified Claims")

        for idx, claim in enumerate(claims_raw.strip().split('\n')):
            claim = claim.strip()
            if not claim:
                continue
            if any(k in claim.lower() for k in ['solve', '=', 'x =', 'discriminant']):
                valid = check_math_step(claim)
            else:
                valid = check_logic_step(claim)
            status = "🟢 Valid" if valid else "🔴 Invalid"
            st.markdown(f"{idx + 1}. {status}: {claim}")
