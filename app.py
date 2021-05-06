import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse("datasets/vaccination_tweets.csv")

st.title('Sentiment Analysis of Covid-19 Vaccine via Social Media')
sidebar = st.sidebar

def analyseTweets():
    with st.spinner("Loading Data ... "):
        st.header('Twitter Accounts')
        # st.plotly_chart(plotBar(analysis.getDataframe(), 'user_verified', "Verified vs unverified"))
        # st.write(analysis.getDataframe())
        st.plotly_chart(piechart(analysis.getDataframe()))
        st.plotly_chart(add_tracePlot(analysis.getDataframe(),))
        #st.plotly_chart(scatterplot(analysis.getDataframe(),))
        st.plotly_chart(barplot1(analysis.getDataframe(),'user_name','total_engagement','total_engagement','Viridis','Accounts per Engagements'))

def analyseTweets():
    with st.spinner("Loading Analysis..."):
        st.header('Verified and Unverified Accounts')
        st.plotly_chart(plotBar(analysis.getDataframe(), 'user_verified', "Verified vs unverified"))

        st.header('Tweet Engagements on the basis of Followers')
        st.plotly_chart(barplot(analysis.getDataframe(), 'acc_class','total_engagement','total_engagement','Rainbow','Engagement By Account_Class'))

        st.header('Media vs No Media Tweets')
        data = analysis.getDataframe()
        st.plotly_chart(plotPie(['Unverified', 'Verified'], data.groupby('med').count()['user_name'].values, 'title'))

        st.header('Length of Tweets')


def analyseSentiments():
    with st.spinner("Loading Analysis..."):
        st.header('Most Used words in Tweets')
        st.image('plotImages/Cloud1.png')

        st.header('Most Used words in Tweets')
        st.image('plotImages/Cloud1_bar.png')

        st.header('Most Used words in Tweets')
        st.image('plotImages/Cloud1.png')

        st.header('Sentiment Count')
        data = analysis.getPolarityCount()
        st.plotly_chart(plotPie(data.index, data.values, 'title'))

        st.plotly_chart(barplot(analysis.getEngagementSentiment(), 'total_engagement', 'sentiment', 'total_engagement', 'Rainbow', 'title'))



def viewForm():

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

def viewDataset():
    st.header('Data used in Analysis')
    st.dataframe(analysis.getDataframe())

sidebar.header('Choose Your Option')
options = [ 'View Dataset', 'Tweets and their account Analysis', 'Sentiment Analysis']
choice = sidebar.selectbox( options = options, label="Choose Action" )
if choice == options[0]:
    viewDataset()
elif choice == options[1]:
    analyseTweets()
elif choice == options[2]:
    analyseSentiments()