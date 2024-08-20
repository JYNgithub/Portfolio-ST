import requests
import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_lottie import st_lottie
from projectcomponents import *

# Page configuration
st.set_page_config(
    page_title = "Chong Jin Jye's Portfolio",
    page_icon= ':bar_chart:',
    initial_sidebar_state="collapsed",
    layout='wide'
)

# Page setup (may not be required)
page_project1 = st.Page(
    page = "pages/HospitalKPIDashboard.py"
)

# Load Font Awesome CSS
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Load custom CSS
def load_css():
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css()

# Load lottie animations
def get_lottie(url):
    link = requests.get(url)
    return link.json()
animation1 = get_lottie("https://lottie.host/f953eec0-8ae0-42d9-a367-cbcf62c3a048/Cja9RYcO4Q.json")
animation2 = get_lottie("https://lottie.host/f6ca40d9-94eb-4400-b894-665f56d4b665/5OfYeb57Wz.json")

# Container 1: Introduction 
with st.container():
    div1, pfp, div2, intro, div3 = st.columns(
        [0.7, 2, 0.7, 5, 0.7]
    )
    
    with div1:
        st.empty()
    with div2:
        st.empty()
    with div3:
        st.empty()
    
    with pfp:
        image = Image.open('assets/pfp.png') # Load and display the image
        st.image(image, use_column_width = True)
        

    with intro:
        st.title("Chong Jin Jye's Portfolio")
        st.write("")
        st.markdown('''
                    <p class="paragraph">
                    If you're here, then either my LinkedIn profile caught your attention, or that my resume passed the ATS. Anyway, welcome to my portfolio!   
                    <br>Check out my list of projects below! </br>
                    </p>
                    ''', unsafe_allow_html = True)
        st.write("")
        st.write("")
        st.markdown(
            '''
            <a href="https://www.linkedin.com/in/chong-jin-jye/" target="_blank">
                <button class="custom-button">
                    <i class="fa-brands fa-linkedin"></i> <!-- Example Font Awesome icon -->
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
        st.caption("Connect with me!")


# Divider
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="height: 25px;"></div>', unsafe_allow_html=True)

# Container 2: Skills & Certs
with st.container():
    div1, skills, certs, animation = st.columns(
        [1.1, 3, 7, 4]
    )
    
    with div1:
        st.empty()
        
    with skills:
        st.header("Skills")
        st.write("""
                - Python
                - SQL
                - Excel
                - Power BI
                - Tableau
                - R
                """)

    with certs:
        st.header("Certifications & Achievements")
        st.write("""
                 - Google Advanced Data Analytics Specialization [(Link)](https://www.coursera.org/account/accomplishments/specialization/52WEGE3U5AAH)
                 - Google Data Analytics Specialization [(Link)](https://www.coursera.org/account/accomplishments/specialization/UB3Z943YTLNG)
                 - ASEAN Data Science Explorer 2024, Participant
                 - TCS Sustainathon Malaysia 2024, Participant
                 - MonsoonSIM Enterprise Resources Management International Competition, Finalist
                 """)
        
    with animation: 
        st_lottie(animation1, width = 350)
        
# Divider
st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="height: 25px;"></div>', unsafe_allow_html=True)

# Container 3: List of Projects
with st.container():

    with st.container():
        div1, animation, selectbox, div2 = st.columns([1,3,5,1])
        with div1: 
            st.empty()  
        with div2:
            st.empty()
        with animation:
            st_lottie(animation2, width = 350)
        with selectbox:
            st.header("List of Projects")
            # Options for select box
            options = ["Select all", "Python", "SQL", "Excel", "Power BI", "Tableau", "R"]
            # Create the select box
            selected_option = st.selectbox("x", options, label_visibility='hidden')
            
            
            # Project details from projectcomponents.py
            if selected_option == "Select all":
                for project_id, details in projects.items():
                    p1, p2 = st.columns([4,1])
                    with p1: 
                        st.markdown(
                            f"""
                            <div class="row">
                                <div class="icon">{details['icon']}</div>
                                <div class="text-container">
                                    <div class="title">{details['title']}</div>
                                    <div class="tools">{', '.join(details['tools_used'])}</div>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    with p2: 
                        st.markdown(
                            """
                            <div class="divider"></div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button(
                            "Learn more",
                            key = f"{project_id}",
                            use_container_width=True
                        ):
                            st.switch_page(f"{details['link']}") 
                    st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)      
            elif selected_option == "Python":
                for project_id, details in projects.items():
                    if "Python" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            elif selected_option == "SQL":
                for project_id, details in projects.items():
                    if "SQL" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            elif selected_option == "Excel":
                for project_id, details in projects.items():
                    if "Excel" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            elif selected_option == "Power BI":
                for project_id, details in projects.items():
                    if "Power BI" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            elif selected_option == "Tableau":
                for project_id, details in projects.items():
                    if "Tableau" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            elif selected_option == "R":
                for project_id, details in projects.items():
                    if "R" in details["tools_used"]:
                        p1, p2 = st.columns([4,1])
                        with p1: 
                            st.markdown(
                                f"""
                                <div class="row">
                                    <div class="icon">{details['icon']}</div>
                                    <div class="text-container">
                                        <div class="title">{details['title']}</div>
                                        <div class="tools">{', '.join(details['tools_used'])}</div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        with p2: 
                            st.markdown(
                                """
                                <div class="divider"></div>
                                """,
                                unsafe_allow_html=True
                            )
                            if st.button(
                                "Learn more",
                                key = f"{project_id}",
                                use_container_width=True
                            ):
                                st.switch_page(f"{details['link']}") 
                        st.markdown('<div class="projectdiv"></div>', unsafe_allow_html=True)
            else:
                st.write("Please select an option.")


    
    with st.container():
        div1, projects, div2 = st.columns([1,8,1])
        with div1:
            st.empty()
        with projects:
            st.empty()
            
            
            

    

            
        
    


