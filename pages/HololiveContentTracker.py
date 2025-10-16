import streamlit as st
from PIL import Image
from projectcomponents import *

def load_css():
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css()

with st.container():
    div1, buttonlocation = st.columns([0.4,11])
    with div1:
        st.empty()
    with buttonlocation:
        returnhome = st.button('Back to Home')
        if returnhome:
            st.switch_page('app.py')

for project_id, details in projects.items():
    if project_id == "project5": ### Update this
        # Container for main image and title
        with st.container():
            div1, mainimage, div2, desc, div3 = st.columns(
                [
                    0.5,5,0.5,6,0.5
                ]
            )
            with div1:
                st.empty()
                
            with mainimage:
                st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
                mainimage = Image.open(f"{details['main_image']}")
                st.image(mainimage, use_container_width = True)
            
            with div2: 
                st.empty()
            
            with desc:
                st.header(f"{details['title']}")
                st.write("")
                st.write("Tools Used: ", f"{', '.join(str(i) for i in details['tools_used'])}")
                st.write("Additional Skills:", f"{', '.join(str(i) for i in details['additional_skills'])}")
                
            with div3:
                st.empty()

        # Divider
        st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
        
        # Container for additional images
        with st.container():
            div1, addimg1, addimg2, addimg3, div2 = st.columns(
                [
                    0.5,3,3,3,5
                ]
            )
            with div1:
                st.empty()
            with div2:
                st.empty()
            with addimg1:
                img1 = Image.open(f"{details['add_image1']}")
                st.image(img1, use_container_width = True)
            with addimg2:
                st.empty()
            with addimg3:
                st.empty()
            
        # Divider
        st.write("---")
        st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)    
               
        # Container for other sections 
        with st.container():
            div1, contents, div2 = st.columns([0.3,6.5,0.3])
            with div1:
                st.empty()
            with div2:
                st.empty()
            with contents:
                st.subheader("Description")
                st.write(f"{details['description']}")
                st.markdown('<div class="imagediv"></div>', unsafe_allow_html=True)
                st.subheader("Resources")
                st.write(f"{details['resources']}")
                st.markdown('<div class="imagediv"></div>', unsafe_allow_html=True)
                st.subheader("Documentation")
                st.write(f"{details['documentation']}")  
            