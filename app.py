# streamlit_app.py

import streamlit as st
from hf_utils import query_hf_model
from reasoning_checker import check_math_step, check_logic_step
from prompts import THINKER_PROMPT, CRITIC_PROMPT

st.set_page_config(page_title="🧠 CoT Verifier", layout="wide")
st.title("🔍 Chain-of-Thought Verifier with Proof Tracing")
st.markdown("Uses **Mistral 7B** via HuggingFace and symbolic tools like **SymPy** and **Z3**.")

question = st.text_area("Enter a question:", height=100, placeholder="E.g., Solve x² + 5x + 6 = 0")

if st.button("Verify"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            thinker_prompt = THINKER_PROMPT.format(question=question)
            raw_reasoning = query_hf_model(thinker_prompt)

        st.markdown("---")
        st.subheader("🧾 Full Reasoning Chain")
        st.code(raw_reasoning)

        with st.spinner("Analyzing Claims..."):
            critic_prompt = CRITIC_PROMPT.format(reasoning=raw_reasoning)
            claim_list = query_hf_model(critic_prompt)

        st.markdown("---")
        st.subheader("🔍 Extracted Claims")
        st.text(claim_list)

        st.markdown("---")
        st.subheader("✅ Verified Claims")

        claims = claim_list.strip().split('\n')
        for idx, claim in enumerate(claims):
            if not claim.strip():
                continue

            if any(kw in claim.lower() for kw in ['solve', 'equation', 'calculate']):
                valid = check_math_step(claim)
            else:
                valid = check_logic_step(claim)

            status = "🟢 Valid" if valid else "🔴 Invalid"
            st.markdown(f"{idx+1}. {status}: {claim}")
