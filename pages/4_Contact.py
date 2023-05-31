import streamlit as st
st.set_page_config(page_title='Prasad Posture',layout='wide',page_icon='logo.ico')

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
[data-testid="collapsedControl"]{
color:#ffffff;
}
[class="css-17lntkn e1fqkh3o5"]{
color:#ffffff;
}
[class="css-1nm2qww e1fqkh3o2"]{
color:#ffffff;
}
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}
</style>

'''

st.markdown(markdown,unsafe_allow_html=True)
st.markdown("""
<h1 style='color:#ffffff; font-family:Times New Roman'>Contact</h1>
<p style='font-family:sheriff; font-size:110%;'>
I am really looking forward to work with you, so if you have any queries regarding the services offered,
my work samples or the pricing, feel free to contact me. Let's grow together.
</p>
<hr style="border-color:#ffffff;">
""", unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/prasadposture121@gmail.com" method="POST">
    <input type="hidden", name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required><br>
    <input type="email" name="email" placeholder="Your Email" required><br>
    <textarea name="message" placeholder="Your Message Here" required></textarea><br>
    <button type="submit">Send</button>
</form>
"""
a,b = st.columns([4,3])
with a:
    st.markdown(contact_form, unsafe_allow_html=True)
with b:
    st.markdown(
        '''
        <p style='font-family:sheriff; font-size:110%;'>
        Follow me on:
        </p>
        <a href="https://www.linkedin.com/in/prasad-posture-6a3a77215/" target="_blank">
        <img src="https://myclouddoor.com/wp-content/uploads/2019/11/Linkedin-logo.png"
        alt="LinkedIn Logo" width="70px" height="40px">
        </a>
        <a href="https://github.com/prasadposture" target="_blank">
        <img src="https://ctl.s6img.com/society6/img/y-xZ_syD7LhIJOGtpdTU08ra6Aw/w_700/prints/~artwork/s6-original-art-uploads/society6/uploads/misc/8e29a2e79387449caa28090d71f489e3/~~/github-logo-prints.jpg?wait=0&attempt=0"
        alt="GitHub Logo" width="40px" height="40px">
        </a> &nbsp &nbsp
        <a href="https://www.kaggle.com/prasadposture121" target="_blank">
        <img src="https://cdn-images-1.medium.com/v2/resize:fit:1200/1*9izrRVNdAJa9bFaqBwSH4w.png"
        alt="Kaggle Logo" width="40px" height="40px">
        </a>
        ''',
        unsafe_allow_html=True
    )


st.markdown("""
<br>
<br>
<br><p class="footer-company-name">All Rights Reserved. &copy; 2023 <a href="#">Prasad Posture</a></p>
""", unsafe_allow_html=True)