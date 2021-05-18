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
# import xgboost
from sklearn import ensemble



pickle_in4 = open("final_model.pkl","rb")
model=pickle.load(pickle_in4)


# import tensorflow as tf
# from tensorflow.keras.models import load_model

def main():
    
    html_temp = """
    <div>
    <h1 style="color:WHITE;text-align:left;"><font size="10"> COVID HOME CARE ⚭ </font></h1>
    </div>
    <style>
    .reportview-container .main{
        background: url("https://i.ibb.co/5KdhhmK/Unknown.jpg");
        background-size: cover;
    }
   .sidebar .sidebar-content {
        background: url("https://i.ibb.co/Sny7Wzm/Mid-shade.png")
    }
    </style>
    <style>
    body {
    background-image: url("https://i.ibb.co/5KdhhmK/Unknown.jpg");
    background-size: cover;
    }
    </style>
    """
    
    
    st.markdown(html_temp, unsafe_allow_html=True)


    # image = Image.open('logo1.jpg')
    # st.image(image, caption=None, width=200, use_column_width=None, clamp=True, channels='RGB', output_format='auto')

    selection = st.sidebar.radio("", ['Introduction','Covid-19 Symtom Checker', 'Health care at Home','Chatbot'])
    st.write("""<style>
            .reportview-container .markdown-text-container {
                font-family: monospace;
            }
            .sidebar .sidebar-content {
                background-image: linear-gradient(#FFFFFF,#FFFFFF);
                color: white;
            }
            .Widget>label {
                color: white;
                font-family: monospace;
            }
            [class^="st-b"]  {
                color: white;
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
        <div style="background-color:{};background: rgba(60, 170, 113, 0.8)">
        <h1 style="color:{};text-align:center;"><b>Covi Bot</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b> The selected 'Chatbot' command will redirect you to an AI bot. You can ask it basic questions like fitness, plasma donation in corona. And in case of any emergency you can asscess the resources as well. </b></font></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
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

        webbrowser.open_new('http://chat2325.herokuapp.com') 
    elif selection == 'Introduction': 
        textbg = """
        <div style="background-color:{};background: rgba(60, 170, 113, 0.8)">
        <h1 style="color:{};text-align:center;"><b>INTRODUCTION</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b> The selected 'Chatbot' command will redirect you to an AI bot. You can ask it basic questions like fitness, plasma donation in corona. And in case of any emergency you can asscess the resources as well. </b></font></h1>
        </div>
        """
        bgcolor = ''
        fontcolor = 'white'
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
        responses=pd.read_csv("responses.csv")  
        df = pd.DataFrame(responses)
        # state_total = get_total_dataframe(df)
        # state_total_graph = px.bar(
        # state_total, 
        # x='Status',
        # y='Number of cases',
        # labels={'Number of cases':'Number of cases in %s' % (select)},
        # color='Status')
        # st.plotly_chart(state_total_graph)
        
        fig = plt.figure(facecolor='white',figsize=(9,5))
        ax = fig.add_subplot(1,1,1)
        ax = df['Blood group:'].value_counts().plot(kind='bar',
                                    figsize=(7,4),
                                    title="Blood groups")
                                 
        ax.set_xlabel("Blood Group")
        ax.set_ylabel("Frequency")
        ax.set_facecolor('black')
        fig2= plt.figure(figsize=(1.5,2))
        ax1 = fig2.add_subplot(1,1,1)
        
        ax1= df['Gender'].value_counts().plot(kind='pie',
                                    figsize=(14,8),
                                    title="Blood groups")
        ax1.set_facecolor('black')
        fig3 = plt.figure(facecolor='white',figsize=(9,5))
        ax2 = fig3.add_subplot(1,1,1)
        ax2 = df['Age'].value_counts().plot(kind='bar',
                                    figsize=(7,4),
                                    title="Age")
                                 
        ax2.set_xlabel("Age")
        ax2.set_ylabel("Frequency")
        ax2.set_facecolor('black')
    
      
        

  
        # X = list(df.iloc[:, 1])
        # Y = list(df.iloc[:, 1])
  

        # p1 =plt.bar(X,Y)
        # plt.title("Students over 11 Years")
        # plt.xlabel("Years")
        # plt.ylabel("Number of Students")
        col1, col2 = st.beta_columns(2)
        col1.write(fig)
        col2.write(fig2)
        col2.write(fig3)
    elif selection == 'Covid-19 Symtom Checker': 
        textbg = """
        <div style="background-color:{};background: rgba(60, 170, 113, 0.8)">
        <h1 style="color:{};text-align:center;"><b>SYMPTOM CHECKER</b></h1>
        </div>
        """
        bgcolor = 'gray'
        fontcolor = 'white'
        st.markdown(textbg.format(bgcolor,fontcolor),unsafe_allow_html=True)

        text = """
        <div style="background-color:{};">
        <h1 style="color:{};text-align:center;"><font size=4><b> The selected 'Chatbot' command will redirect you to an AI bot. You can ask it basic questions like fitness, plasma donation in corona. And in case of any emergency you can asscess the resources as well. </b></font></h1>
        </div>
        """
        bgcolor = ''
        fontcolor = 'white'
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
        Fever = st.sidebar.selectbox("Fever",("Yes","No"))
        tiredness = st.sidebar.selectbox("Tiredness",("Yes","No"))
        pain = st.sidebar.selectbox("Pain",("Yes","No"))
        diahria = st.sidebar.selectbox("Diarrhea",("Yes","No"))
        dry = st.sidebar.selectbox("Dry-Cough",("Yes","No"))
        breath = st.sidebar.selectbox("Difficulty-in-Breathing",("Yes","No"))
        soar = st.sidebar.selectbox("Sore-Throat",("Yes","No"))
        nose = st.sidebar.selectbox("Running nose",("Yes","No"))
        nasal = st.sidebar.selectbox("Nasal-Congestion",("Yes","No"))
        age = st.sidebar.selectbox("Age",("0-9","10-19","20-25","26=59","60+"))
        gender= st.sidebar.selectbox("Gender",("Male","Female","Other"))

        if Fever == 'Yes':
            Fever = 1
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
        else :
            diahria= 0

        if dry == 'Yes':
            dry= 1
        else :
            dry = 0
        if soar== 'Yes':
            soar= 1
        else :
            soar= 0
        if breath == 'Yes':
                breath= 1
        else :
            breath = 0
        if nose== 'Yes':
            nose= 1
        else :
            nose = 0
        if nasal== 'Yes':
            nasal= 1
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
        # if result==0:
        #     result = 'Mild'
        # elif result==1:
        #     result = 'None to Mild'
        # elif result==2:
        #     result = 'Moderate'

        st.success('Your severity is {}'.format(result))

  
  

        

        
if __name__ == '__main__':
    main()


