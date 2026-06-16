import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Healthcare FAQ Chatbot",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Healthcare FAQ Chatbot")

st.sidebar.header("💡 Example Questions")

example_question = st.sidebar.selectbox(
    "Choose an example question:",
    [
        "What causes mental illness?",
        "What are some of the warning signs of mental illness?",
        "What is glaucoma?",
        "What causes glaucoma?",
        "What are the symptoms of glaucoma?",
        "What is stomach cancer?"
    ]
)

user_query = st.text_input(
    "Ask a healthcare-related question...",
    value=example_question
)

if st.button("Get Answer"):
    if user_query.strip():
        with st.spinner("Searching for the best answer..."):
            result = get_response(user_query)

        if result["found"]:
            st.subheader("🎯 Matched Question")
            st.success(result["question"])

            st.subheader("💡 Answer")
            with st.expander("Click to view the full answer", expanded=False):
                st.markdown(result["answer"], unsafe_allow_html=False)

            if result["found"]:
                st.subheader("📊 Similarity Score")
                st.metric("Score", f"{result['score']:.4f}")
                
            if result["score"] >= 0.80:
                st.success("High confidence match")
            elif result["score"] >= 0.50:
                st.info("Moderate confidence match")
            else:
                st.warning("Low confidence match")
        else:
            st.info("No matching question found.")
            st.warning(result["answer"])
                
    else:
        st.warning("⚠️ Please enter a healthcare-related question.")

st.markdown("---")
st.caption(
    "🚀 Built with Python • NLTK • Scikit-learn (TF-IDF + Cosine Similarity) • Streamlit"
)