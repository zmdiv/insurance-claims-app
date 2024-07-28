import streamlit as st
import requests

st.title("Insurance Claims Processor")

st.header("Upload your files")
insurance_file = st.file_uploader("Upload Insurance Coverage (PDF)", type=["pdf"])
medical_reports = st.file_uploader("Upload Medical Reports and Receipts", type=["pdf", "jpg", "png"])

if st.button("Submit"):
    if insurance_file and medical_reports:
        files = {
            "insurance_file": ("insurance_file.pdf", insurance_file.getvalue(), "application/pdf"),
            "medical_reports": ("medical_reports.pdf", medical_reports.getvalue(), "application/pdf" if medical_reports.type == "application/pdf" else "image/jpeg")
        }
        response = requests.post("http://localhost:8000/process", files=files)
        st.write(response.json())
    else:
        st.error("Please upload both files")
