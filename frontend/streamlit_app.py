import streamlit as st
import requests
import time

st.title("Insurance Claims Processor")

st.header("Upload your files")
insurance_files = st.file_uploader("Upload Insurance Coverage (PDF)", type=["pdf"], accept_multiple_files=True)
medical_reports = st.file_uploader("Upload Medical Reports and Receipts", type=["pdf", "jpg", "png"], accept_multiple_files=True)

if st.button("Submit"):
    if insurance_files and medical_reports:
        summary_results = []
        for insurance_file in insurance_files:
            for medical_report in medical_reports:
                files = {
                    "insurance_file": ("insurance_file.pdf", insurance_file.getvalue(), "application/pdf"),
                    "medical_reports": ("medical_reports", medical_report.getvalue(), medical_report.type)
                }
                response = requests.post("http://localhost:8000/process", files=files)
                if response.status_code == 200:
                    result = response.json()
                    summary_results.append(result)
                else:
                    st.error("Error processing files")
                
                time.sleep(1)  # Add a slight delay to simulate processing
        st.write("Summary of Results:")
        for idx, result in enumerate(summary_results, 1):
            st.write(f"Result {idx}: {result}")
    else:
        st.error("Please upload both files")
