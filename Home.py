import streamlit as st
from PIL import Image
st.set_page_config(page_title='Prasad Posture',layout='wide', page_icon='logo.ico')

markdown='''
<style>
[data-testid="stAppViewContainer"]{
background-color:#000000;
color:#ffffff;
}
[data-testid="stHeader"]{
opacity:0.0;
}
[data-testid="stSidebar"]{
background-color:#171717
}
[class="css-pkbazv e1fqkh3o5"]{
color:#ffffff
}
[class="css-17lntkn e1fqkh3o5"]{
color:#ffffff
}
[data-testid="collapsedControl"]{
color:#ffffff;
}
[class="css-1nm2qww e1fqkh3o2"]{
color:#ffffff;
}
</style>
'''

st.markdown(markdown,unsafe_allow_html=True)



a,b = st.columns([3,2])
with a:
    content='''
<br>
<h1 style="font-size:330%; text-align:center; color:#ffffff; font-family:Times New Roman">PRASAD POSTURE</h1>
<br>

<p style="font-family:monospace; font-size:120%; text-align:center; color:#ffffff;">"Freelance Data Analyst, Python Programmer, <br>
Notebook Expert, Astronomy Enthusiast."<br>
<br>
<a href='https://www.linkedin.com/in/prasad-posture-6a3a77215/' target='blank'><img align='center' src='https://img.shields.io/badge/-Prasad Posture-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/prasad-posture-6a3a77215/'  height='20' width='100' /></a>
<a href='https://github.com/prasadposture' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/prasadposture'  height='20' width='100' /></a>
<a href='https://www.kaggle.com/prasadposture121' target='blank'><img align='center' src='https://img.shields.io/badge/-prasadposture121-blue?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/prasadposture121' height='20' width='100' /></a>

</p>
<br>
<br>
<p style="font-size:140%; border:1px solid gray; border-radius:15px; text-align:center; width:300px">
Contact me for<br></p>
<p>
<b> Question Based Analysis, &nbsp Exploratory Data Analysis<br>
    Interactive Dashboards, &nbsp Web Applications, &nbsp Predictive Modeling
</b>
</p>
'''
    st.markdown(content, unsafe_allow_html=True)

with b:
    img =  Image.open('images\cbg.jpg')
    st.image(img)
