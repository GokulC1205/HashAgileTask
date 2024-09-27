**Resume Information Extractor:**

Resume Information Extractor is a tool designed to extract essential details from resumes in various formats (PDF, DOCX, TXT) using Streamlit and Google Gemini API. This project was created as part of the Hash Agile selection process.

**Features:**

**Multi-Format Support:** Upload and extract text from resumes in PDF, DOCX, or TXT formats.

**AI-Powered Extraction:** Utilizes Google Gemini to accurately identify and extract key information such as Name, Email, Phone Number, College Name, Skills.

**Database Integration:** Stores extracted resume details in MongoDB for easy access and management.

**User-Friendly Interface:** Built with Streamlit to provide an intuitive and responsive user experience.

**Clean Output:** Displays extracted information in a well-formatted table for easy readability.

**Technologies Used:**

- Python
- Streamlit
- Google Generative AI (Langchain)
- PDFMiner
- Python-docx
- Texttable
- MongoDB (for data storage)
- dotenv (for environment variable management)

**Do with me:**
To run this project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-information-extractor.git
   cd resume-information-extractor

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ``` bash
   streamlit run Resume_extraction.py
**Sample Output**
![Screenshot (607)](https://github.com/user-attachments/assets/fe0a575d-4bc4-43aa-addb-b9354826d651)

