import os
from PyPDF2 import PdfReader
import pdfplumber
from docx import Document
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for PDFs with images

def extract_text_from_pdf(filepath):
    """Extract text from PDF files."""
    try:
        text = ""
        # Use PyMuPDF for better formatting
        with fitz.open(filepath) as pdf:
            for page in pdf:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def extract_text_from_word(filepath):
    """Extract text from Word files."""
    try:
        doc = Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"Error reading Word file: {e}")
        return None

def extract_text_from_image(filepath):
    """Extract text from image files using OCR."""
    try:
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error reading Image: {e}")
        return None

def process_resume(filepath):
    """Process resume based on file type."""
    file_ext = os.path.splitext(filepath)[-1].lower()

    if file_ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif file_ext in [".doc", ".docx"]:
        return extract_text_from_word(filepath)
    elif file_ext in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(filepath)
    else:
        print(f"Unsupported file type: {file_ext}")
        return None

# Example Usage
if __name__ == "__main__":
    filepath = "C:/Users/jesli/Downloads/Jeslin_Resume.pdf"  # Replace with your file path
    extracted_text = process_resume(filepath)
    if extracted_text:
        print(extracted_text)
    else:
        print("Failed to extract text.")
