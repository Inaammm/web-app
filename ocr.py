from PIL import Image
import pytesseract

# Set the Tesseract path directly



def extract_text(image):
    """
    Extract text from the given image using pytesseract.
    """
    try:
        text = pytesseract.image_to_string(image, lang='eng+hin+kan+tel')
        return text.strip()  # Remove leading and trailing whitespace
    except Exception as e:
        return f"Error extracting text: {e}"

# Example usage
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    image = Image.open(image_path)
    extracted_text = extract_text(image)
    print(extracted_text)
