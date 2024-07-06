import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import re

class ResumeEvaluator:
    @staticmethod
    def extract_text(pdf):
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=200,
            length_function=len)
        
        segments = text_splitter.split_text(text=text)
        return segments

    @staticmethod
    def analyze_with_ai(api_key, segments, query):
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        vector_store = FAISS.from_texts(segments, embedding=embeddings)
        relevant_docs = vector_store.similarity_search(query=query, k=3)
        ai_model = ChatOpenAI(model='gpt-3.5-turbo', api_key=api_key)
        qa_chain = load_qa_chain(llm=ai_model, chain_type='stuff')
        result = qa_chain.run(input_documents=relevant_docs, question=query)
        return result

    @staticmethod
    def generate_overview_query(content):
        return f"""
        Provide the output in the following format:

        **Key qualifications and skills (top 3-5)**
        - [Skill 1]
        - [Skill 2]
        - [Skill 3]

        **Most relevant work experience (1-2 sentences)**
        - [Brief description of most relevant experience]

        **Educational background (if notable)**
        - [Brief description of education]

        **Standout achievements or unique selling points**
        - [Achievement or unique selling point]

        Be specific and quantitative where possible. 
        Tailor your analysis for a busy hiring manager who needs to quickly grasp the candidate's potential.

        Resume content:
        {content}
        """

    @staticmethod
    def generate_highlights_query(content):
        return f"""
        Provide the output in the following format:

        **Top 3 key strengths of the candidate**
        - [Strength 1]: [Brief explanation]
        - [Strength 2]: [Brief explanation]
        - [Strength 3]: [Brief explanation]

        **Top 2 unique selling points**
        - [Unique selling point 1]
        - [Unique selling point 2]

        **Top 2 specific examples supporting strengths and selling points**
        - [Example 1]
        - [Example 2]

        Please be concise and focus on the most impactful elements. 

        Resume content:
        {content}
        """

    @staticmethod
    def generate_improvement_query(content):
        return f"""
        Provide the output in the following format:

        **Potential areas of concern or red flags (2-3)**
        - [Concern 1]: [Brief explanation]
        - [Concern 2]: [Brief explanation]
        - [Concern 3]: [Brief explanation]

        **Critical missing information**
        - [Missing information 1]
        - [Missing information 2]

        Provide brief explanations for each point. 

        Resume content:
        {content}
        """

    @staticmethod
    def display_formatted_output(title, content):
        # Replace Markdown asterisks with HTML bold tags
        formatted_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
        
        # Split the content into sections
        sections = re.split(r'\n(?=<strong>)', formatted_content)
        
        html_output = f"<div class='output-text'><h4>{title}</h4>"
        
        for section in sections:
            # Extract section title and content
            match = re.match(r'<strong>(.*?)</strong>(.*)$', section, re.DOTALL)
            if match:
                section_title, section_content = match.groups()
                html_output += f"<h5 style='color: #4A90E2;'>{section_title.strip()}</h5>"
                
                # Split content into bullet points
                bullet_points = re.findall(r'-\s*(.*?)(?=\n-|\n<strong>|\Z)', section_content, re.DOTALL)
                
                if bullet_points:
                    html_output += "<ul>"
                    for point in bullet_points:
                        html_output += f"<li>{point.strip()}</li>"
                    html_output += "</ul>"
            else:
                # If no section title, just add the content as a paragraph
                html_output += f"<p>{section.strip()}</p>"
        
        html_output += "</div>"
        st.markdown(html_output, unsafe_allow_html=True)

    @staticmethod
    def display_resume_overview():
        if st.session_state.pdf is not None and st.session_state.api_key:
            try:
                with st.spinner('Analyzing the resume...'):
                    pdf_segments = ResumeEvaluator.extract_text(st.session_state.pdf)
                    overview_query = ResumeEvaluator.generate_overview_query(pdf_segments)
                    overview = ResumeEvaluator.analyze_with_ai(st.session_state.api_key, pdf_segments, overview_query)
                ResumeEvaluator.display_formatted_output("Candidate Overview", overview)
            except Exception as e:
                st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Error: {e}</h5>', unsafe_allow_html=True)
        elif st.session_state.pdf is None:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please upload a resume</h5>', unsafe_allow_html=True)
        elif not st.session_state.api_key:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please enter your OpenAI API Key in the sidebar</h5>', unsafe_allow_html=True)

    @staticmethod
    def display_resume_highlights():
        if st.session_state.pdf is not None and st.session_state.api_key:
            try:
                with st.spinner('Identifying candidate strengths...'):
                    pdf_segments = ResumeEvaluator.extract_text(st.session_state.pdf)
                    highlights_query = ResumeEvaluator.generate_highlights_query(pdf_segments)
                    highlights = ResumeEvaluator.analyze_with_ai(st.session_state.api_key, pdf_segments, highlights_query)
                ResumeEvaluator.display_formatted_output("Candidate Strengths", highlights)
            except Exception as e:
                st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Error: {e}</h5>', unsafe_allow_html=True)
        elif st.session_state.pdf is None:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please upload a resume</h5>', unsafe_allow_html=True)
        elif not st.session_state.api_key:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please enter your OpenAI API Key in the sidebar</h5>', unsafe_allow_html=True)

    @staticmethod
    def display_improvement_suggestions():
        if st.session_state.pdf is not None and st.session_state.api_key:
            try:
                with st.spinner('Evaluating potential concerns...'):
                    pdf_segments = ResumeEvaluator.extract_text(st.session_state.pdf)
                    improvement_query = ResumeEvaluator.generate_improvement_query(pdf_segments)
                    improvements = ResumeEvaluator.analyze_with_ai(st.session_state.api_key, pdf_segments, improvement_query)
                ResumeEvaluator.display_formatted_output("Areas of Concern", improvements)
            except Exception as e:
                st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Error: {e}</h5>', unsafe_allow_html=True)
        elif st.session_state.pdf is None:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please upload a resume</h5>', unsafe_allow_html=True)
        elif not st.session_state.api_key:
            st.markdown(f'<h5 style="text-align: center;color: #4A90E2;">Please enter your OpenAI API Key in the sidebar</h5>', unsafe_allow_html=True)
