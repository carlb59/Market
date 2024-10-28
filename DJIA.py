import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from dash.dash_table.Format import Format, Group, Scheme, Symbol
import datetime as dt

djia = pd.read_csv('/home/maison/Documents/Eco/DJIA.csv', sep=',',skiprows=1, header=None, decimal=',', thousands='.', names=['Date', 'Close'])
djia['Date']=pd.to_datetime(djia['Date'])
djia['Month']=djia['Date'].dt.to_period('M')
djia_m = djia.groupby('Month').mean('Close').reset_index()

fig = px.line(djia, x='Date', y='Close', log_y=True)

app = Dash(__name__)

app = DJIA.server

app.layout = html.Div(children=[
    html.H1(children='DJIA Daily Close'),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
