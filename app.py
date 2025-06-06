import streamlit as st
from verifier import cot_verifier_pipeline

st.set_page_config(page_title="🧠 CoT Verifier", layout="wide")
st.title("🔍 Chain-of-Thought Verifier with Proof Tracing")

question = st.text_area("Enter a question:", height=100, placeholder="E.g., Solve x² + 5x + 6 = 0")

if st.button("Verify"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Verifying..."):
            claims, raw = cot_verifier_pipeline(question)

        st.markdown("---")
        st.subheader("🧾 Full Reasoning Chain")
        st.code(raw)

        st.markdown("---")
        st.subheader("✅ Verified Claims")
        for idx, claim in enumerate(claims):
            status = "🟢 Valid" if claim["valid"] else "🔴 Invalid"
            st.markdown(f"{idx+1}. {status}: {claim['claim']}")
