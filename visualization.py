import plotly.graph_objects as go
import plotly.express as px

def plotBar(df, x, title):

    fig = px.bar(df, x=x, title=title)
    return fig

def plotLine(df, x, y, title):
    fig = px.line(df, x, y)

    return fig