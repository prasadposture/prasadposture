import streamlit as st
from PIL import Image
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
[data-baseweb="tab"]{
padding: 10px 10px 10px 10px;
border:1px solid gray;
border-radius: 5px;
}
[data-baseweb="tab-highlight"]{
opacity:0.0;
}
[data-testid="stImage"]{
border:1px solid gray;
border-radius:5px;
padding: 5px 5px 5px 5px;
}
[data-testid="caption"]{
color:#ffffff;
}
[data-testid="stExpander"]{
border: 1px solid gray;
border-radius:5px;
}
[class="stMarkdown"]{
color:#ffffff;
}

</style>

'''

st.markdown(markdown,unsafe_allow_html=True)
st.markdown("""
<h1 style='color:#ffffff; font-family:Times New Roman'>Portfolio</h1>
<p style='font-family:sheriff; font-size:110%;'>
To learn more about my services, please see some of my relevant projects linked below.
I have worked on vairety of projecs, while taking new approaches of looking at the data.
I am confident that I can help you get the most out of your data.
<hr style="border-color:#ffffff;">
""", unsafe_allow_html=True)
listTabs = ['   QBA & EDA   ', '   Interactive Dashboards   ','   Web Applications   ','   Predictive Modeling   ']
a,b,c,d = st.tabs(listTabs)
with a:
    ab, ac, ad, ae = st.columns(4)
    with ab:
        img3 = Image.open('images\ipl.png')
        st.image(img3, caption='EDA of IPL Mathces (2008-20)')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            Cricket is the most popular sport in India.
            There are various formats of this game and
            the most loved is the IPL. In this project,
            I have analyzed the data related to IPL matches
            from year 2008 to 2020. My aim was to draw useful
            insights and look out for the major factors that help
            teams win the matches. I used pandas & numpy
            for data manipulation and matplotlib & seaborn for data visualization.
            I learned all these things for free from
            a course offered by jovian.ai and did this project under that course.
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/exploratory-data-analysis-of-ipl-matches">Checkout the project</a>
            """, unsafe_allow_html=True)
    with ac:
        img1 = Image.open('images\Data-Science.jpeg')
        st.image(img1,caption="Analysis of Data Science Jobs")
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            The field of data scienc experiencing immense growth 
            and the need for analyzing mammoth amount of data is increasing day-by-dat.
            There are various job titles among this field and to understand
            about them, here I have data of 3755 job titles from the companies
            all across the world. I have perform question based analysis to
            generate various insights and to see what are the main factors
            that affect the relation of job titles and their salaries.
            You can find it in both Excel and jupyter notebook format.
            <p>
            <a href="https://github.com/prasadposture/Analysis-of-Data-Science-Jobs">Checkout the project</a>
            """, unsafe_allow_html=True)
    with ad:
        img2 = Image.open('images\covid19.png')
        st.image(img2, caption="Covid-19 Data Analysis")
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            It contains analysis of spread of covid-19 virus all across the country.
            I used the data of each state to analyze the total number of cases, total deaths, population of the state
            and all the other relevant attributes. In addition to that it also contains beautiful visuals
            that convey the findings easily.
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/covid-19-data-analysis">Checkout the project</a>
            """, unsafe_allow_html=True)
    with ae:
        img4 = Image.open('images\kaggle.jpg')
        st.image(img4, caption='Kaggle ML & DS Survey')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            In this project, I used kaggle's official data of the survey.
            The dataset contains each question of the survey as a column. I have
            done analysis of those questions, and found some interesting things about the kaggle users.
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/kaggle-s-ml-and-ds-survey-2022">Checkout the project</a>
            """, unsafe_allow_html=True)
with b:
    ba, bc, bd, be = st.columns(4)
    with ba:
        img5 = Image.open('images\ipl.png')
        st.image(img5, caption='IPL Mathces Dashboard')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            This project uses similiar data that I had used for EDA of IPL Matches, the difference is that
            here I have represented my findings using PowerBI dashboard. The dashboard additionally contains
            measures like strike rate, total runs scored, batting average, economy, wickets taken, bowling average
            of the players which can be filtered year-wise and venue-wise. It can potentially help teams to pick
            players with good perfomance for a particular match.
            <p>
            <a href="https://github.com/prasadposture/EDA-of-IPL-Matches">Checkout the project</a>
            """, unsafe_allow_html=True)
    with bc:
        img6 = Image.open('images\house-price.jpg')
        st.image(img6, caption='House Price (Visualization)')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            Here, it contains the data visulization section of streamlit web app that predicts sale price of house
            given the attribute. Since made with programming language this dashboard is flexbile and can be manipulated
            according to our needs. Also it's easy to access from anywhere you want. The interactive visuals make it
            whole lot easier to understand the inter-relationship of the attributes.
            <p>
            <a href="https://prasadposture-house-prices-advanced-regression-t-1--home-of41rn.streamlit.app/Visualization">Checkout the project</a>
            """, unsafe_allow_html=True)
with c:
    ca, cb, cd, ce = st.columns(4)
    with ca:
        img7 = Image.open('images\kfinance.jpg')
        st.image(img7, caption='Financial Distress Prediction')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            Financial distress prediction is a key issue
            in measuring corporate solvency. Its main objective
            is to distinguish normal companies from those at risk of
            financial distress. For enterprises themselves, financial
            distress prediction can help to identify risks early,
            make plans according to the actual situation, and adjust business strategy.
            This streamlit web-app makes use of trained machine learning model to predict
            whether somebody will face financial distress within next two years based on their
            past and current conditions.
            <p>
            <a href="https://prasadposture-financial-distress-prediction-fdp-7abgw6.streamlit.app/">Checkout the project</a>
            """, unsafe_allow_html=True)
    with cb:
        img8 = Image.open('images\house-price.jpg')
        st.image(img8, caption='House Price Prediction')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            This user friendly application predicts sale price of the houses based on the different attributes
            related to a house. It makes use of two machine learning model which are trained
            and tuned over the data of 1460 houses and it provides great accuracy. In addition to that it contains different kind of visuals
            that help understand the relationship better.
            <p>
            <a href="https://prasadposture-house-prices-advanced-regression-t-1--home-of41rn.streamlit.app/">Checkout the project</a>
            """, unsafe_allow_html=True)
    with cd:
        img9 = Image.open('images\water.jpg')
        st.image(img9, caption='Water Potability')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            The potability of water is not decided by a single factor but by the contribution of all factors
            This web application takes amount of different water constituents as input and predicts
            whether it is potable or not. A user could play around and determine the ranges till the combination
            of amount of water constituents keeps it potable.
            <p>
            <a href="https://prasadposture-water-potability-proj-water-potability-app-zvgixo.streamlit.app/">Checkout the project</a>
            """, unsafe_allow_html=True)
    with ce:
        img10 = Image.open('images\RandomForest.jpg')
        st.image(img10, caption='RandomForestClassifier')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            This is my first ever streamlit web application. I had built it for kaggle competitions. In here you can drag and drop or upload
            the competition datasets and then the application will itself do all the necessary work such as filling missing values,
            label encoding, dropping unnecessary columns and make predictions on the dataset. It has proven to be given
            a great accuracy and will be helpful for beginner who wants to compare their model.
            <p>
            <a href="https://prasadposture-randomforestclassfi-randomforestclassifier-sy515c.streamlit.app/">Checkout the project</a>
            """, unsafe_allow_html=True)
with d:
    da, db,dc, de = st.columns(4)
    with da:
        img11 = Image.open('images\kfinance.jpg')
        st.image(img11, caption='Financial Distress Prediction')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            It's a jupyter notebook created under Machine Learning Course offered by Jovian.ai.
            Here I do predictive analysis and on the data for predicting whether someone will face financial distress
            within next two years or not. I have compared multiple models with their base accuracy and trained the one with highest accuracy.
            It makes use of classification algorithms, which are used for predicting discrete variables.
        
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/financial-distress-prediction">Checkout the project</a>
            """, unsafe_allow_html=True)
    with db:
        img12 = Image.open('images\house-price.jpg')
        st.image(img12, caption='House Price Prediction')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            This notebook contains EDA and MLA of the data contains information about the different attributes of the houses
            and their selling price. This notebook has completed 2000+ views and was featured on kaggle's official website.
            It is very beginner friendly and uses new approaches such as weighted Average Ensemble for higher accuracy.
            It uses regression algorithms, which are used for predicting continuous variables.
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/house-prices-prediction">Checkout the project</a>
            """, unsafe_allow_html=True)
    with dc:
        img13 = Image.open('images\water.jpg')
        st.image(img13, caption='Water Potability')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            I had created this notebook as the part of my 5th semester project in Jai Hind College, Mumbai. It uses 
            Decision Tree Classifier which also a classification algorithm and predicts water is potable or not. In addition to
            it, I have tuned the hyper-parameter so that the model can do better predictions on the unseen data as well. Theh confusion
            matrix at end gives us better understanding of the model's performance.
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/water-potability-project">Checkout the project</a>
            """, unsafe_allow_html=True)
    with de:
        img14 = Image.open('images\galaxy.png')
        st.image(img14, caption='Stellar Classification')
        with st.expander('Click to see more'):
            st.markdown("""
            <p style='font-family:sheriff; font-size:95%;'>
            The space, the stars, the galaxies are always my favorite topic of studies.
            It makes use of clustering algorithms to predict whether the given data is about a star, a quasar or
            a galaxy. Though the labels are given I used K-Nearest Neighbours which is a part of unsupervised learning
            to create 3 clusters of from the given datasets and late compare them with the labels. The model showed accuracy of 0.65
            which is great for an unsupervised model. 
            <p>
            <a href="https://www.kaggle.com/code/prasadposture121/stellar-classification">Checkout the project</a>
            """, unsafe_allow_html=True)