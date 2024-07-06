import streamlit as st
from utils import get_base64_of_bin_file

def setup_page():
    st.set_page_config(page_title='TalentScan AI: Resume Analyzer for HR professionals', layout="wide")
    
    st.markdown("""
    <style>
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .logo-title {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: -10px;
    }
    .subtitle {
        margin-top: 0;  /* Remove top margin from subtitle */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-container">
        <div class="logo-title">
            <img src="data:image/png;base64,{}" alt="TalentScan AI Logo" style="width: 60px; margin-right: 15px;">
            <h1 style="color: #4A90E2; margin: 0;">TalentScan AI</h1>
        </div>
        <h3 class="subtitle" style="color: #4A90E2; text-align: center;">Efficient Candidate Evaluation for Enterprise</h3>
    </div>
    """.format(get_base64_of_bin_file("logo.png")), unsafe_allow_html=True)