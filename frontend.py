import streamlit as st
from backend import Backend, TextAnalysisResult

def main():
    st.set_page_config(page_title="AI Text Detection Tool", layout="wide")
    st.title("AI Text Detection Tool")

    backend = Backend()

    # Sidebar with file uploader
    with st.sidebar:
        st.header("Upload Text File")
        uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
        st.info("Upload a .txt file to analyze if the text is AI-generated or human-written.")

    # Main content
    if uploaded_file is not None:
        with st.spinner("Analyzing text..."):
            result: TextAnalysisResult = backend.process_file(uploaded_file)
        
        if result.error:
            st.error(result.error)
        else:
            st.subheader("Analysis Result")
            st.write(f"**AI-Generated**: {'Yes' if result.is_ai_generated else 'No'}")
            st.write(f"**Confidence**: {result.confidence:.2%}")
            st.progress(result.confidence)

if __name__ == "__main__":
    main()