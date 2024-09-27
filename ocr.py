from PIL import Image
import pytesseract

def extract_text(image):
    """
    Extract text from the given image using pytesseract.
    """
    text = pytesseract.image_to_string(image, lang='eng+hin+kan+tel')
    return text
