import pdfplumber

class PDFParser:
    def parse_pdf(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
