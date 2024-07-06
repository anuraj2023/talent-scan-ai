# TalentScan AI: Resume Analyzer for HR Professionals

## Project Overview

TalentScan AI is a powerful resume analysis tool designed for HR professionals to streamline the candidate evaluation process. Leveraging advanced natural language processing and machine learning techniques, TalentScan AI provides quick, insightful analyses of resumes, helping recruiters identify top candidates efficiently. 

You can try out this app here : https://talent-scan-ai.streamlit.app/

## Key Features

- **Resume Overview**: Generates a concise summary of key qualifications, skills, and experiences.
- **Candidate Strengths**: Identifies and highlights the top strengths and unique selling points of each candidate.
- **Areas of Concern**: Flags potential issues or missing information in the resume.
- **User-Friendly Interface**: Built with Streamlit for an intuitive, web-based user experience.
- **AI-Powered Analysis**: Utilizes OpenAI's GPT models for intelligent resume parsing and evaluation.

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework for the user interface
- **LangChain**: Framework for developing applications powered by language models
- **OpenAI API**: Provides the GPT-3.5-turbo model for natural language processing
- **PyPDF2**: Library for reading and extracting text from PDF files
- **FAISS**: Vector database for efficient similarity search of text embeddings
- **Streamlit-Option-Menu**: Custom component for creating a sidebar navigation menu
- **Streamlit-Extras**: Additional Streamlit components for enhanced UI elements

## Implementation Details

1. **PDF Processing**: 
   - Resumes in PDF format are uploaded and processed using PyPDF2.
   - Text is extracted and split into manageable chunks using LangChain's text splitter.

2. **Text Embedding**:
   - Extracted text chunks are converted into vector embeddings using OpenAI's embedding model.
   - These embeddings are stored in a FAISS vector database for efficient retrieval.

3. **AI Analysis**:
   - Specific queries are generated for each analysis type (overview, strengths, concerns).
   - LangChain's question-answering chain is used to process these queries against the relevant resume sections.
   - OpenAI's GPT-3.5-turbo model provides detailed, context-aware responses.

4. **User Interface**:
   - Streamlit is used to create a responsive, user-friendly web interface.
   - The UI includes a sidebar for resume upload and API key input, and a main area for displaying analysis results.
   - Streamlit-Option-Menu creates a custom navigation sidebar for different analysis views.

5. **Output Formatting**:
   - Analysis results are post-processed to convert markdown formatting to HTML.
   - Custom CSS is applied to style the output for improved readability.

## System Architecture

[![](https://mermaid.ink/img/pako:eNqVlN9v2jAQx_8Vy33ZJIqA0AGZNCkQoBSm0dHuYc0ejH0hVoMdObYKavu_z0kcVvZDU_Jw8tmfO-e-d_IzppIB9nGcyieaEKXRXRgJZL_g4V2E73NQaCE0qJhQiPD7H77vG14R44cIr8MZWitJIc-52EW4OOciM7pCJhYJ1gsUGJ2A0JwSzaWoMGL3Kiq01B0cNJoetCL0F5JVmStqWlOTxIjH021nzOyUab8Fxv4OzYvKZsFis0HfgGqpUDh2pTGiyZbkUIHXNtutAXVEcxCgyD9-bGGxFRG7SUK4QLcBKhcVSKVyyW4cZcgO0GereupkcGou7flXyDMpcvhD0rP7VpacSbUnWgNDX4wu5C4xWa2F6yC6vPz0EuFuG91nqSQM2W5F-AWNz897bdtiG4eKTi3hWCCTc8Rrow2kViwUCJIec54X0LWbgwJCYWmnpZ2Vdu5ULJ2F0_6tM3nrLErnprTL0q5KG9Tl0JTkeQgxMhzFPE39i3jEBl3ayrWSj-BfeJ7n1pdPnOnE72WHj7_FlrN5Ch92PdIovJhZF92FYY-NGkW7LtYJRturD4NGCerxdBm2nase7TTKUMyji_b6oyHbNiu_Vh4Gfeo1U76azVr6Lu134v_H4xbeg510zuwb9VzsRNi-JHv7FPl2ySAmJrXDH4lXi9ruyM1RUOxrZaCFlTS7BPsxSXPrmczKByEnO0X2NZIR8V1K577-BG_xmA4?type=png)](https://mermaid.live/edit#pako:eNqVlN9v2jAQx_8Vy33ZJIqA0AGZNCkQoBSm0dHuYc0ejH0hVoMdObYKavu_z0kcVvZDU_Jw8tmfO-e-d_IzppIB9nGcyieaEKXRXRgJZL_g4V2E73NQaCE0qJhQiPD7H77vG14R44cIr8MZWitJIc-52EW4OOciM7pCJhYJ1gsUGJ2A0JwSzaWoMGL3Kiq01B0cNJoetCL0F5JVmStqWlOTxIjH021nzOyUab8Fxv4OzYvKZsFis0HfgGqpUDh2pTGiyZbkUIHXNtutAXVEcxCgyD9-bGGxFRG7SUK4QLcBKhcVSKVyyW4cZcgO0GereupkcGou7flXyDMpcvhD0rP7VpacSbUnWgNDX4wu5C4xWa2F6yC6vPz0EuFuG91nqSQM2W5F-AWNz897bdtiG4eKTi3hWCCTc8Rrow2kViwUCJIec54X0LWbgwJCYWmnpZ2Vdu5ULJ2F0_6tM3nrLErnprTL0q5KG9Tl0JTkeQgxMhzFPE39i3jEBl3ayrWSj-BfeJ7n1pdPnOnE72WHj7_FlrN5Ch92PdIovJhZF92FYY-NGkW7LtYJRturD4NGCerxdBm2nase7TTKUMyji_b6oyHbNiu_Vh4Gfeo1U76azVr6Lu134v_H4xbeg510zuwb9VzsRNi-JHv7FPl2ySAmJrXDH4lXi9ruyM1RUOxrZaCFlTS7BPsxSXPrmczKByEnO0X2NZIR8V1K577-BG_xmA4)

## Setup and Usage

1. Clone the repository and install dependencies:
   ```
   git clone git@github.com:anuraj2023/talent-scan-ai.git
   cd talent-scan-ai
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key as an environment variable or input it in the app's sidebar.

3. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

4. Upload a resume PDF and use the sidebar navigation to explore different analyses.

## Future Enhancements

- Integration with applicant tracking systems (ATS)
- Customizable evaluation criteria for different job roles
- Batch processing of multiple resumes
- Enhanced data visualization for comparative candidate analysis

## Contributors

- Anuraj Suman

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
