import streamlit as st

from analyzer import analyze_claim


st.set_page_config(
    page_title="CogniGuard",
    page_icon="🛡️",
    layout="centered"
)


st.title("🛡️ CogniGuard")
st.caption("AI-Powered Misinformation Risk Analyzer")

st.markdown(
    """
    CogniGuard analyzes news claims using a local LLM and
    retrieval-based knowledge to identify potential warning signals.
    """
)

st.divider()


claim = st.text_area(
    "📝 Enter a news claim or statement",
    placeholder=(
        "Example: Scientists have discovered a medicine "
        "that can cure every disease."
    ),
    height=160
)


if st.button("🔍 Analyze Claim", use_container_width=True):

    if not claim.strip():

        st.warning("Please enter a claim before analyzing.")

    else:

        with st.spinner("🧠 Analyzing with AI + RAG..."):

            result = analyze_claim(claim)

        st.success("Analysis completed!")

        st.divider()

        st.subheader("🧠 AI Analysis")

        st.write(result["reason"])

        st.divider()

        st.info(
            "⚠️ CogniGuard provides AI-assisted analysis and "
            "should not be treated as a final factual verdict. "
            "Important claims should be verified using reliable sources."
        )