import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

#setting layout
st.set_page_config(layout ="wide")

#setting lottiefile
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coder = load_lottieurl("https://lottie.host/e0a0520e-9ce5-41bc-86ee-0f604143507d/JFqswOzHOC.json")
lottie_project = load_lottieurl("https://lottie.host/ab83be21-1188-45fb-8b4b-f98eba37b2d2/pecZUJy3pf.json")
lottie_contact = load_lottieurl("https://lottie.host/cba9cc01-bf2e-4d89-a5f5-cc48115d5ff9/qTZQrVVChc.json")

#sidebar 
st.write("##")
st.subheader("Hey guys :wave:")
st.title("My Portfolio website")


with st.container():
    selected = option_menu(
        menu_title =  "Main Menu",
        options=['About','Projects','Contact'],
        icons = ['person-circle','code-slash','chat-left-text-fill'],
        orientation = 'horizontal'
    )
    
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Dharshini S")
            st.title("Here is some information about me")
        with col2:
             st_lottie(lottie_coder)
             

    
    with st.container ():
         col3, col4 = st.columns(2)
         with col3:
            st.subheader("""
            Education 
            - KGISL institue of technology
                - B.Tech AI&DS 
            - Vivekananda Matric Higher Secondary School
                - HSC and SSLC
            - Good at
                - Pencil Art 
                - Photography
                - puzzle solving
            """)
         with col4:
             st.subheader("""
             Interested and currently learning
             - Python 
             - Hackathon
             - Digital marketing
             """)
             
if selected == "Projects":
    with st.container():
        st.header("My projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st_lottie(lottie_project, height= 300)
        with col6:
            st.subheader("TIC-TAC-TOE")
            st.markdown("[Visit Github Repo : TIC-TAC-TOE](https://stlit-tic-tac-toe-2dw6zzp8tan35hude6xsru.streamlit.app/)")
            st.markdown("[Visit Github Repo : GUESSING-GAME](https://guessing-game-1.streamlit.app/)")
            
if selected == "Contact":
    st.header("Connect with : ")
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.write("[Connect with me on LinkedIn](https://www.linkedin.com/in/dharhsini-s-80993b314?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )")
        st.write("[My_GitHub_Profile](https://www.linkedin.com/in/dharhsini-s-80993b314?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )")
    with right_col:
        st_lottie(lottie_contact, height = 300)
        
