import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def plotBar(df, x, title):

    fig = px.bar(df, x=x, title=title)
    return fig

def plotLine(df, x, y, title):
    fig = px.line(df, x, y)

    return fig

def barplot(df,x,y,color,color_continuous_scale,title):
    class_eng = df.groupby(x, as_index=False).agg({y:'sum',})
    fig = px.bar(class_eng,
             x=x,
             y=y,
             color=color,
             color_continuous_scale=color_continuous_scale,
             title=title)
    return fig

def piechart(df):
    Media = len(df[df['med']=='Media'])
    No_Media = len(df[df['med']=='No Media'])
    Platform = ['Media','No Media']
    Count = [Media,No_Media]
    #====
    fig = px.pie(names = Platform,
                values = Count,
                title='Media/No Media',
                color_discrete_sequence = px.colors.sequential.Rainbow)
    fig.update_traces(textposition='inside', textinfo='percent+label')