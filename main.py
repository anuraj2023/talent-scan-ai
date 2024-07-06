import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from ui_setup import setup_page
from resume_evaluator import ResumeEvaluator

def main():
    setup_page()
    add_vertical_space(5)

    if 'pdf' not in st.session_state:
        st.session_state.pdf = None

    with st.sidebar:
        add_vertical_space(4)
        if 'api_key' not in st.session_state:
            st.session_state.api_key = ''
        
        st.markdown('<h3 style="color: #4A90E2;">Settings</h3>', unsafe_allow_html=True)
        api_key = st.text_input("Enter your OpenAI API Key:", type="password", key="api_key_input")
        if api_key:
            st.session_state.api_key = api_key

        add_vertical_space(2)
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
        if uploaded_file is not None:
            st.session_state.pdf = uploaded_file

        add_vertical_space(2)
        option = option_menu(menu_title='', options=['Overview', 'Strengths', 'Concerns'],
                             icons=['file-earmark-text', 'star-fill', 'exclamation-triangle-fill'],
                             styles={
                                "container": {"background-color": "#1E1E1E"},
                                "icon": {"color": "#4A90E2"},
                                "nav-link": {"color": "#FFFFFF", "font-size": "14px"},
                                "nav-link-selected": {"background-color": "#4A90E2"},
                             })

    if option == 'Overview':
        ResumeEvaluator.display_resume_overview()
    elif option == 'Strengths':
        ResumeEvaluator.display_resume_highlights()
    elif option == 'Concerns':
        ResumeEvaluator.display_improvement_suggestions()

if __name__ == "__main__":
    main()