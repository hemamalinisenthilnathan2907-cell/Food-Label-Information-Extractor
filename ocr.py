import pytesseract
import shutil


# Find Tesseract automatically
tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    # Windows local path
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text
