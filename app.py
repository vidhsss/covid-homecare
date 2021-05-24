import streamlit as st
import numpy as np
import pandas as pd
import time
import os
import pickle
import shutil
# import plotly.graph_objects as go
from PIL import Image
# from plotly.subplots import make_subplots
from PIL import Image, ImageOps
import numpy as np
# import base64
# import path
import json
import streamlit.components.v1 as components
import webbrowser 
import time 
import matplotlib.pyplot as plt
import pickle 
import sklearn
from gnewsclient import gnewsclient
# import xgboost
from sklearn import ensemble

import joblib
# from newsapi import NewsApiClient
# from music_recommendation import recommendSongs,ENCODER,song_data,SONGS


from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn.feature_extraction.text import CountVectorizer

def get_title_from_index(index):
      return df.loc[index, "original_title"]
def get_rating_from_index(index):
  return df.loc[index, "original_title"],df.loc[index, "reviews_from_users"]

def get_index_from_title(original_title):
  return df.loc[df.original_title == original_title].index[0]

# pickle_in4 = open("movie.pkl","rb")
# cosine_sim1=pickle.load(pickle_in4)
# df=pd.read_csv("movies.csv")

# newsapi = NewsApiClient(api_key='c9e5723356c24681b8ad6fcdd86566dc')
# query= input("keyword")


vect = CountVectorizer(max_features=1000, binary=True)
pickle_in4= open("news.pkl","rb")
nb=pickle.load(pickle_in4)

vect= joblib.load("vectorizer.pkl")
def pred(X_test) : 
    X_test_vect = vect.transform(X_test)

    y_pred = nb.predict(X_test_vect)
    

    return y_pred


pickle_in4 = open("model3.pkl","rb")
model=pickle.load(pickle_in4)


# import tensorflow as tf
# from tensorflow.keras.models import load_model

def main():
    
    html_temp = """
    <div >
    <h1 style="color:BLACK;text-align: center; "><font size="10"> COVID HOME CARE ⚭ </font></h1>
    </div>
    <style>
    .reportview-container .main{
        background: url("https://i.ibb.co/DM13tnz/pngtree-blue-simple-solid-color-background-color-image-48192.jpg" );
        background-size: cover;
    }
   .sidebar .sidebar-content {
        background: url("https://i.ibb.co/DM13tnz/pngtree-blue-simple-solid-color-background-color-image-48192.jpg")
    }
    </style>
    <style>
    body {
    background-image: url("https://i.ibb.co/DM13tnz/pngtree-blue-simple-solid-color-background-color-image-48192.jpg");
    background-size: cover;
    }
    </style>
    """
    
    
    st.markdown(html_temp, unsafe_allow_html=True)


    # image = Image.open('logo1.jpg')
    # st.image(image, caption=None, width=200, use_column_width=None, clamp=True, channels='RGB', output_format='auto')

    selection = st.sidebar.radio("", ['Introduction','Covid-19 Symptom Checker','Chatbot','News','Recommendations'])
    st.write("""<style>
            .reportview-container .markdown-text-container {
                font-family: monospace;
            }
            .sidebar .sidebar-content {
                background-image: linear-gradient(#FFFFFF,#FFFFFF);
                color: black;
            }
            .Widget>label {
                color: black;
                font-family: monospace;
            }
            [class^="st-b"]  {
                color: black;
                font-family: monospace;
            }
            .st-bb {
                background-color: transparent;
            }
            .st-at {
                
            }
            footer {
                font-family: monospace;
            }
            .reportview-container .main footer, .reportview-container .main footer a {
                color: #FFFFFF;
            }
            header .decoration {
                background-image: none;
            }
            </style>""", unsafe_allow_html=True)

    if selection == 'Chatbot':
        textbg = """
        <div style="background-color:{};background: #3A3985">
        <h1 style="color:{};text-align:center;"><b>Covi Bot</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'black'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b> The selected 'Chatbot' command will redirect you to an AI bot. You can ask it basic questions like fitness, plasma donation in corona. And in case of any emergency you can asscess the resources as well. </b></font></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'black'
        st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#3CB371,#3CB391);
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,)

        webbrowser.open_new('http://chat2325.herokuapp.com') 
   
    elif selection == 'Covid-19 Symptom Checker': 
        textbg = """
        <div style="background-color:{};background: rgba(60, 170, 113, 0.8)">
        <h1 style="color:{};text-align:center;"><b>SYMPTOM CHECKER</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'black'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b> Check the severity of your symtoms and also know some precautions.</b></font></h1>
        </div>
        """
        bgcolor = ''
        fontcolor = 'black'
        st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#3CB371,#3CB391);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,) 
        Fever = st.sidebar.selectbox("Fever",("No","Yes"))
        tiredness = st.sidebar.selectbox("Tiredness",("No","Yes"))
        pain = st.sidebar.selectbox("Chest Pain",("No","Yes"))
        diahria = st.sidebar.selectbox("Diarrhea or gastrointestinal symptoms",("No","Yes"))
        dry = st.sidebar.selectbox("Dry-Cough",("No","Yes"))
        breath = st.sidebar.selectbox("Difficulty-in-Breathing",("No","Yes"))
        soar = st.sidebar.selectbox("Sore-Throat",("No","Yes"))
        nose = st.sidebar.selectbox("Running nose",("No","Yes"))
        nasal = st.sidebar.selectbox("Nasal-Congestion",("No","Yes"))
        age = st.sidebar.selectbox("Age",("0-9","10-19","20-25","26=59","60+"))
        gender= st.sidebar.selectbox("Gender",("Male","Female","Other"))

        if Fever == 'Yes':
            Fever = 1
            text = """
            <div style="background-color:{};">
            <h1 style="color:{};text-align:left;"><font size=5><b>For Fever: </b></font></h1>
            </div>
            """
            bgcolor = 'light grey'
            fontcolor = 'white'
            st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
            st.write("Patients can take paracetamol or ibuprofen when self-medicating for symptoms of COVID-19, such as fever and headache")
        else :
            Fever = 0

        if tiredness == 'Yes':
            tiredness= 1
        else :
            tiredness= 0

        if pain == 'Yes':
            pain = 1
        else :
            pain = 0

        if diahria == 'Yes':
            diahria= 1
            text="""
            <div style="background-color:{};">
            <h1 style="color:{};text-align:left;"><font size=5><b>For Gastrointestinal Symptoms: </b></font></h1>
            </div>
            """
            bgcolor = ''
            fontcolor = 'white'
            st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
            st.write("You can treat the digestive symptoms of COVID-19 at home by staying hydrated, avoiding foods that upset your stomach, and getting as much rest as possible.")
        else :
            diahria= 0

        if dry == 'Yes':
            dry= 1
            text="""
            <div style="background-color:{};">
            <h1 style="color:{};text-align:left;"><font size=5><b>For Dry Cough: </b></font></h1>
            </div>
            """
            bgcolor = ''
            fontcolor = 'white'
            st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
            st.write("Cough medicines or cough suppressants can help reduce your cough. Throat lozenges and remedies like honey and lemon may improve a sore throat.")
        else :
            dry = 0
        if soar== 'Yes':
            soar= 1
            text="""
            <div style="background-color:{};">
            <h1 style="color:{};text-align:left;"><font size=5><b>For Soar Throat: </b></font></h1>
            </div>
            """
            bgcolor = ''
            fontcolor = 'white'
            st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
            st.write("Drink plenty of fluids to stay hydrated while you recover. Warm liquids like broths or tea with honey may help to soothe throat irritation and soreness.\n\nTry gargling with a salt water solution to help lessen sore throat pain.")
        else :
            soar= 0
        if breath == 'Yes':
                breath= 1
                text="""
                <div style="background-color:{};">
                <h1 style="color:{};text-align:left;"><font size=5><b>For Difficulty in breathing</b></font></h1>
                </div>
                """
                bgcolor = ''
                fontcolor = 'white'
                st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
                st.write("Take slow breaths. Slowing things down can help you start breathing again properly.\n\nTry relaxation or meditation techniques. These will help calm the body and get your breathing more regular. Additionally, having shortness of breath may leave you feeling anxious. These relaxation techniques will help fight the anxiety.\n\nIf you were previously prescribed an inhaler, you may need to use it. Pay attention to how your chest feels and what symptoms your inhaler was prescribed for. Do not use someone else's inhaler – only use one that is prescribed to you. Make sure you disinfect the mouthpiece after every use.")
        else :
            breath = 0
        if nose== 'Yes':
            nose= 1
            
        else :
            nose = 0
        if nasal== 'Yes':
            nasal= 1
            text="""
                <div style="background-color:{};">
                <h1 style="color:{};text-align:left;"><font size=5><b>For Nasal Congestion </b></font></h1>
                </div>
                """
            bgcolor = ''
            fontcolor = 'white'
            st.markdown(text.format(bgcolor,fontcolor),unsafe_allow_html=True)
            st.write("If your symptoms are mild, you can try a few different techniques that help relieve sinus pressure from a stuffy nose, like steam from a humidifier, nasal irrigation via neti pots or nasal sprays, or a bit of decongestant")
        else :
            nasal = 0
        if gender=="male":
            male=1
            female=0
            trans=0
        elif gender=="female": 
            male=0
            female=1
            trans=0
        else: 
            male=0
            female=0
            trans=1
        if age=="0-9":
            ans=[[Fever,tiredness,dry,breath,soar,pain,nasal,nose,diahria,1,0,0,0,0,female,male,trans]]
        elif age=="10-19": 
            ans=[[Fever,tiredness,dry,breath,soar,pain,nasal,nose,diahria,0,1,0,0,0,female,male,trans]]
        elif age=="20-25": 
            ans= ans=[[Fever,tiredness,dry,breath,soar,pain,nasal,nose,diahria,0,0,1,0,0,female,male,trans]]
        elif age=="26-59": 
            ans=[[Fever,tiredness,dry,breath,soar,pain,nasal,nose,diahria,0,0,0,1,0,female,male,trans]]
        else : 
            ans=[[Fever,tiredness,dry,breath,soar,pain,nasal,nose,diahria,0,0,0,0,1,female,male,trans]]

        df = pd.DataFrame(ans, columns = ['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing', 'Sore-Throat', 'Pains', 'Nasal-Congestion', 'Runny-Nose', 'Diarrhea',  'Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+', 'Gender_Female', 'Gender_Male', 'Gender_Transgender'])
        result=""
        
        if st.button("Predict"):
            result=model.predict(df)
        if result==0:
            result = 'Moderate.\n\n '
        elif result==1:
            if breath==1 or pain==1:
                result='Moderate to severe.\n\nIt is advised to seek help'
            else :
             result = 'None to Mild.\n\n '
        elif result==2:
            result = 'Moderate to severe.\n\nIt is advised to seek help'
        elif result==3: 
            result='Moderate to Severe. \n\nIt is advised to seek help'
        

        st.success('Your severity is {}'.format(result))
        st.write("If your illness is worsening or your symptoms haven't improved after seven days, you should seek medical attention as soon as possible")
        st.write("Some helpline nos:\n \nThe national helpline no: 1075\n\nE sanjeevini: +91-11-23978046\n\nFree Counseling support: 1800-599-0019")
    elif selection == 'News': 
        textbg = """
        <div style="background-color:{};background: rgba(60, 170, 113, 0.8)">
        <h1 style="color:{};text-align:center;"><b>News on Go</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b>NEWS  </b></font></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#3CB371,#3CB391);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,) 
        categor = st.selectbox(
        'Choose a Category',
        (        ('Top Stories','World','Nation','Business','Technology','Entertainment','Sports','Science','Health')))

        query=st.text_input("Any keywords to search:")
        
        countr= st.radio ("",['World','India'])
        if countr=='India':  
            
            # top_headlines = newsapi.get_top_headlines(
            # category=categor,
            # language='en',
            # country='in',
            # q=query
            # )
            client = gnewsclient.NewsClient(language='english', 
                                location='India', 
                                topic=categor)
        elif countr=='World' :
            
            # top_headlines = newsapi.get_top_headlines(
            # category=categor,
            # language='en',
            # q=query
            # )
            client = gnewsclient.NewsClient(language='english', 
                                topic=categor,
                                max_results=10)

        # for article in top_headlines['articles']:
            
        
        #     description=article['title']
        #     y=pred([description])
        #     if y==1 or y==2 : 
        #         if "Deaths" or "died" or "die" not in description: 
        #             st.success('Title : {}\n\n Description : {} \n\nContinue reading at: {} '.format(article['title'],article['description'],article['url']))
        news_list = client.get_news()
        for article in news_list:
            description=article['title']
            y=pred([description])
            if y==1 or y==2 : 
                if "Deaths" or "died" or "die" not in description: 
                   st.success('Title : {}\n\n Description : {} \n\nContinue reading at: {} '.format(article['title'],article['description'],article['link']))
            

    
    elif selection == 'Introduction': 
        textbg = """
        <div style="background-color:{};background:  #3A3985">
        <h1 style="color:{};text-align:center;"><b>Health care tips </b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

       
        
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#3CB371,#3CB391);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,)           
        st.write("If you are sick with COVID-19 or think you might have COVID-19, follow the steps below to care for yourself and to help protect other people in your home and community.")

       
        st.write("\n\n")
        st.info("🏠 STAY HOME (except to get medical care)")
        st.write("  1. Stay home. Most people with COVID-19 have mild illness and can recover at home without medical care. Do not leave your home, except to get medical care. Do not visit public areas.\n\n  2. Take care of yourself. Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel better.\n\n  3. Stay in touch with your doctor. Call before you get medical care. Be sure to get care if you have trouble breathing, or have any other emergency warning signs, or if you think it is an emergency.")
        st.info("🛏  SEPARATE YOURSEELF FROM OTHER PEOPLE")
        st.write("As much as possible, stay in a specific room and away from other people and pets in your home. If possible, you should use a separate bathroom. If you need to be around other people or animals in or outside of the home, wear a mask.\n\n Tell your close contacts that they may have been exposed to COVID-19. An infected person can spread COVID-19 starting 48 hours (or 2 days) before the person has any symptoms or tests positive. By letting your close contacts know they may have been exposed to COVID-19, you are helping to protect everyone.")
        st.info("🌡 MONITOR YOUR SYMTOMS")
       
        st.write("Symptoms of COVID-19 include fever, cough, or other symptoms.\n\nFollow care instructions from your healthcare provider and local health department. Your local health authorities may give instructions on checking your symptoms and reporting information.")
        st.subheader("Emergency warning signs:")
        st.write("✒︎ Chest pain or pressuretrouble breathing\n\n✒︎ Shortness of breath\n\n ✒︎Bluish lips, fingers or toes, or skin\n\n ✒︎Trouble waking up or staying awake\n\n✒ New confusion")
        st.text("*This list is not all possible symptoms. Please call your medical provider for any other\n symptoms that are severe or concerning to you.")
        st.info("  THINGS YOU IMMIDIATELY NEED")
        st.write("(select the things you dont have):")
        if st.checkbox("OXYMETER"): 
            link='available at [click here](https://www.amazon.in/s?k=oxymeter&ref=nb_sb_noss_2)'
            st.markdown(link,unsafe_allow_html=True)
        if st.checkbox("Thermometer"): 
            link='available at [click here](https://www.amazon.in/s?k=thermometer&ref=nb_sb_noss_2)'
            st.markdown(link,unsafe_allow_html=True)
        if st.checkbox("Hospital Grade sanitiser"):  
            link='available at [click here](https://www.amazon.in/s?k=hospital+grade+sanitiser&dc&ref=a9_sc_1)'
            st.markdown(link,unsafe_allow_html=True)
        if st.checkbox("Disposable cutlery "): 
            link='available at [click here](https://www.amazon.in/s?k=disposable+cutlery&ref=nb_sb_noss_2)'
            st.markdown(link,unsafe_allow_html=True)

        if st.checkbox("Steam machine"): 
            link='available at [click here](https://www.amazon.in/FH-FRATELLO-HOME-Vaporizer-vaporizer/dp/B0933PWTWC/ref=sr_1_1_sspa?dchild=1&keywords=steam+machine&qid=1621550981&sr=8-1-spons&psc=1&smid=A2E8NKVQGMNIVM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVlM4WjRQSUVWQlRPJmVuY3J5cHRlZElkPUEwMzI3NzU2MTIzOEo4TjFDS1RFNCZlbmNyeXB0ZWRBZElkPUEwMDk2NzI5Q0tJTVMxM0g1VERRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)'
            st.markdown(link,unsafe_allow_html=True)
        st.text("* All these can also be availed at local medics shop\n\n\n")
    
    elif selection == 'Recommendations': 
        textbg = """
        <div style="background-color:{};background:  #3A3985">
        <h1 style="color:{};text-align:center;"><b>RECOMMENDATIONS </b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

       
        
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#3CB371,#3CB391);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,)  
        selection1 = st.sidebar.radio("", ['General','Movies','Music'])
        if selection1=='Movies' : 
            st.header("MOVIE RECOMMENDATION")
            df=pd.read_csv("movies.csv")
            
            movie_user_likes = st.text_input("Search the movie for which you want recommendations for: ")
            try:
                movie_index = get_index_from_title(movie_user_likes.upper())
        # Compile similar movies based on cosine similarity
                similar_movies = list(enumerate(cosine_sim1[movie_index]))
                sorted_similar_movies = sorted(similar_movies,key=lambda x: x[1], reverse=True)
                i=0
                col1, col2 = st.beta_columns(2)
                col1.info("MOVIES")
                col2.info("USER RATINGS")
                for movie in sorted_similar_movies:
                    
                    col1.text(get_rating_from_index(movie[0])[0])
                    col2.text(get_rating_from_index(movie[0])[1])
                    i=i+1
                    if i>15:
                        break
            except: 
                st.text("Please write a valid movie name")
        elif selection1=='Music' : 
            st.header("MUSIC RECOMMENDATION")
            col1, col2 = st.beta_columns(2)

            name=" "
            
            name=str(col1.text_input("Search the song name"))
            
            try:
                num=ENCODER [(name)]
                test = song_data.values[num]
                recommend = recommendSongs(test)
        
                # recommend_sort=sorted(recommend,key=lambda x: x[1])
                for song in recommend:
                    # print(song)
                    st.write(SONGS.loc[song, "name"])
            except: 
                st.write("")
                # st.text("write a valid song name")

        elif selection1=='General' : 
            st.write("It can be anxious staying in a room for days. Being happy and in high sprits is as important as being healthy. Below are few pass time activities you can get yourself engaged in during quarantine: ")
            st.info("1.Get reading")
            st.write("Read your favourite book and get lost in your imagination.")
            st.info("2.Virtual socialising")
            st.write("Just because you can’t gather in close quarters with your friends doesn’t mean you can’t socialise (virtually, at least)")
            st.info("3.Clean up")
            st.write("'Kondo-ing' your home has been shown to carry many benefits. Clutter makes it harder for us to focus on tasks, so should you find yourself working from home, a quick tidy up might help you to get your jobs done. A messy bedroom has been linked with difficulty sleeping, and messy kitchens with making poor health choices, like reaching for junk food. If you are going to be spending more time in the house, it will be worth your while getting your living spacesin order.")
            st.info("4.Play online games")
            st.write("You can play online games with starangers like ludo, chess,skriblo")
            st.info("5.Watch movies")
            st.write("Watching good contnt can be refreshing.You can find suggestions to watch movie of your choice in movies section")
            st.info("6.Listen to music")
            st.write("Listening to music can ease your mind and can incuce cheerfulness. Get recommendations in the music section")

        
if __name__ == '__main__':
    main()


