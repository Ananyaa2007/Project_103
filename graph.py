import pandas as pd
import plotly.express as px 

df = pd.read_csv("covidData.csv")

fig = px.scatter(df, x= "date", y="cases",color="country", size_max=40, title = "COVID-19 Cases' Graph")
fig.show()