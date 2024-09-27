import streamlit as st
from ocr import extract_text
from search import search_keyword
from PIL import Image

st.title("OCR for English Hindi and Kannada Telugu Text")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text
    extracted_text = extract_text(image)
    st.write("Extracted Text:")
    st.text(extracted_text)

    # Search functionality
    search_query = st.text_input("Enter keyword to search:")
    if search_query:
        result = search_keyword(extracted_text, search_query)
        st.write(result)
