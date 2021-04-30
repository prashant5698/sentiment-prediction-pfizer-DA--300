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

st.title('Global Warming and Climate Change Analysis')
sidebar = st.sidebar

def analyseTweets():
    st.header('Tweets Analysis')

    st.plotly_chart(plotBar(analysis.getDataframe(), 'user_verified', "Verified vs unverified"))
    st.write(analysis.getDataframe())
    st.plotly_chart(barplot(analysis.getDataframe(), 'acc_class','total_engagement','total_engagement','Rainbow','Engagement By Account_Class'))
    st.plotly_chart(piechart(analysis.getDataframe(),))

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

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Analyse Tweets', 'View Report' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

if choice == options[1]:
    analyseTweets()
elif choice == options[2]:
    viewReport()