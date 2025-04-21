from preswald import text, plotly
import pandas as pd
import plotly.express as px

def separate_box_plots(df):
    text("### Temperature Distribution by Star Type")
    fig1 = px.box(df, x='Star Type', y='Temperature', color='Star Type')
    fig1.update_layout(height=400, width=800, showlegend=False)
    plotly(fig1)
    
    text("### Luminosity Distribution by Star Type")
    fig2 = px.box(df, x='Star Type', y='Luminosity', color='Star Type')
    fig2.update_layout(height=400, width=800, showlegend=False)
    plotly(fig2)