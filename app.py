import streamlit as st
import pymupdf

def extract_text_from_pdf(uploaded_file):
    pdfbytes = uploaded_file.read()
    document = pymupdf.open(
        stream = pdfbytes,
        filetype= "pdf"
    )
    text = ""
    for page in document:
        text += page.get_text()

    document.close()

    return text

st.set_page_config(
    page_title="EvalRAG AI",
    page_icon="🤖",
    layout="wide"
)

st.title("EvalRAG AI")
st.subheader("RAG Evaluation & Observability Platform")

st.write(
    "Upload documents, ask questions, and evaluate "
    "AI-generated responses."
)

uploaded_file = st.file_uploader(
    "Upload a document",
    type = ["pdf", "text"]
)

if uploaded_file is not None:
    st.success("Document uploaded successfully.")
    st.write("File name", uploaded_file.name)
    st.write("File type", uploaded_file.type)
    st.write("File size", uploaded_file.size, "bytes")

    extracted_text = extract_text_from_pdf(uploaded_file)

    st.subheader = "Extracted Text Preview"
    st.text(extracted_text[:2000])