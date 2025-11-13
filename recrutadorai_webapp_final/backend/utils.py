import docx
import PyPDF2

def extract_text_from_file(path):
    if path.lower().endswith(".pdf"):
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif path.lower().endswith(".docx"):
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""
