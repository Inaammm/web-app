OCR Web Application for Hindi and English Text
Project Overview
This project demonstrates the ability to perform Optical Character Recognition (OCR) on images containing text in both Hindi and English. The extracted text is displayed on a simple web interface, and users can search for specific keywords within the text. The application is built using Python, Streamlit (for the web interface), and Tesseract (for OCR).

Features
Image Upload: Users can upload an image containing Hindi , English , and kannada , telugu text.
Text Extraction: The application uses Tesseract OCR to extract text from the image.
Keyword Search: Users can search for specific words within the extracted text.
Live Web Application: The application is deployed and accessible online.
Live Demo
Try the live application here: Live Demo Link

Tech Stack
Python: Core programming language.
Tesseract OCR: For text extraction.
Streamlit: To build the web interface.
Gradio (Optional): For an alternative web interface.
Huggingface Transformers: Can be integrated for advanced OCR models.
Prerequisites
Make sure you have the following installed on your system:

Python 3.8+
Tesseract OCR
pip (Python package manager)
Local Setup Instructions

Step 1: Clone the Repository

 

Step 2: Set Up Virtual Environment

Create and activate a virtual environment (optional but recommended):


Step 3: Install Dependencies

Install all required dependencies listed in requirements.txt:


pip install -r requirements.txt

Step 4: Install Tesseract

If Tesseract OCR is not installed on your machine, follow the instructions below:

Windows: Download and install Tesseract from here. After installation, add the Tesseract installation folder (e.g., C:\Program Files\Tesseract-OCR\) to your system's PATH.
Linux: Install Tesseract using:
bash
Copy code
sudo apt install tesseract-ocr
Mac: Install Tesseract via Homebrew:
bash
Copy code
brew install tesseract




Step 5: Run the Application
Run the application using Streamlit:


step 6 :streamlit run app.py
This will start the web app, and you can view it locally at http://localhost:8501.

Project Structure
ocr-web-app/

│
├── app.py                # Main Streamlit app

├── ocr.py                # OCR logic (text extraction using Tesseract)

├── search.py             # Keyword search logic

├── requirements.txt      # Python dependencies

├── README.md             # Project documentation

├── test_images/          # Sample test images

├── models/               # Optional, store model files

└── .gitignore            # Files to ignore in Git








Deployment

Option 1: Deploy on Streamlit Cloud

Create an account at Streamlit Cloud.

Link your GitHub repository and select the app.py file as the main entry point.

Deploy the application and get the live URL.




Example Usage
Upload Image: Upload a .jpg or .png image containing Hindi and English text.

Extracted Text: The OCR will extract the text and display it on the page.

Keyword Search: Enter a word or phrase in the search box to find it within the extracted text.

Screenshots
Upload Image and View Extracted Text:

Keyword Search in Extracted Text:

Future Enhancements
Integration of more advanced OCR models (like Qwen2-VL, GOT) using Huggingface Transformers.
Multi-language support for more languages beyond Hindi and English.
Adding more features such as sentence-by-sentence translation or summary generation.
Contributing
Contributions are welcome! If you have any suggestions or would like to contribute, please create a pull request or issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Tesseract OCR
Streamlit# OCR-web-app
