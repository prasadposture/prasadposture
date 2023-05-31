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
st.markdown("""
<h1 style='color:#ffffff; font-family:Times New Roman'>Services</h1>
<p style='font-family:sheriff; font-size:110%;'>
As a freelance data analyst, I provide a wide range of services to help businesses and individuals better understand
their data. With total three years of experience (2 years of academics + 1 year of personal projects) in the field,
I have developed a strong skillset in Data Cleaning and Manipulation, Data Analysis (EDA & QBA), Data Visualization,
Predictive Analysis. Here's the more information about my individual service, for the relevant project check the portfolio
tab. For any queries related to services or pricing, feel free to contact.
</p>
<hr style="border-color:#ffffff;">
""", unsafe_allow_html=True)

a,b = st.columns(2)
with a:
    st.markdown(
        """
        <h4 style='color:#ffffff;
        text-align:center;
        background-color:#282c35 ;'>
        Question Based Analysis (QBA)
        </h4>
        <p style='color:#ffffff;
        background-color:#171717;
        font-family:sheriff; font-size:100%;
        padding: 10px 10px 10px 10px;'>
        Question-based analysis is one of my core strengths.
        I work with clients to identify key questions they have about their data,
        and then use a combination of statistical techniques and data visualization tools to provide answers.
        Whether you're looking to understand customer behavior, identify trends,
        or optimize your business operations,
        I can help.<br>
        <b>Tools Used:</b> &nbsp Excel, PowerQuerry, Python, Python Libraries
        <p>
        """,
        unsafe_allow_html=True
    )
with b:
    st.markdown(
        """
        <h4 style='color:#ffffff;
        text-align:center;
        background-color:#282c35 ;'>
        Exploratory Data Analysis (EDA)
        </h4>
        <p style='color:#ffffff;
        background-color:#171717;
        font-family:sheriff; font-size:100%;
        padding: 10px 10px 10px 10px;'>
        Exploratory data analysis is another area where I excel.
        By using a combination of tools and data manipulation techniques,
        I can quickly identify patterns and trends in your data.
        This can help you make better decisions and gain a deeper understanding of your business.
        This service can be integrated with QBA and it contains complicated visuals such as 3D ScatterPlot, Heatmap,
        Starbust, etc.<br>
        <b>Tools Used:</b> &nbsp Python, Python Libraries
        <br>
        <br>
        <p>
        """,
        unsafe_allow_html=True
    )

a,b,c = st.columns(3)
with a:
    st.markdown(
        """
        <h4 style='color:#ffffff;
        text-align:center;
        background-color:#282c35;'>
        Interactive Dashboards
        </h4>
        <p style='color:#ffffff;
        background-color:#171717;
        font-family:sheriff; font-size:100%;
        padding: 10px 10px 10px 10px;'>
        Interactive dashboards are a great way to visualize data
        and make it more accessible and user friendly. I can create custom dashboards
        that allow you to explore your data in real-time.
        This can help you identify trends and patterns that you might otherwise miss.<br>
        <b>Tools Used:</b> &nbsp PowerBI, Python, Python Libraries
        <br>
        <br>
        <br>
        <br>
        <p>
        """,
        unsafe_allow_html=True
    )
with b:
    st.markdown(
        """
        <h4 style='color:#ffffff;
        text-align:center;
        background-color:#282c35;'>
        Web Applications
        </h4>
        <p style='color:#ffffff;
        background-color:#171717;
        font-family:sheriff; font-size:100%;
        padding: 10px 10px 10px 10px;'>
        Web applications are another area where I have experience.
        I can create custom web apps that allow you to interact with your data in new and innovative ways with user friendly interfece.
        Whether you're looking to create a custom reporting tool or a data-driven marketing campaign, I can help.<br>
        <b>Tools Used:</b> &nbsp Python, Python Libraries (Mainly Streamlit & Plotly)
        <br>
        <br>
        <p>
        """,
        unsafe_allow_html=True
    )
with c:
    st.markdown(
        """
        <h4 style='color:#ffffff;
        text-align:center;
        background-color:#282c35 ;'>
        Predictive Modeling
        </h4>
        <p style='color:#ffffff;
        background-color:#171717;
        font-family:sheriff; font-size:100%;
        padding: 10px 10px 10px 10px;'>
        I have experience with predictive modeling.
        This involves using machine learning algorithms
        to predict future outcomes based on historical data.
        This can be incredibly powerful, and can help you make more
        informed decisions about your business. Based on the type / presence of ouput variable,
        I can use classification, regression, or clustering algorithms.<br>
        <b>Tools Used:</b> &nbsp Machine Learning Algorithms
        <p>
        """,
        unsafe_allow_html=True
    )
