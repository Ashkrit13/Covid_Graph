import pandas as pd
import plotly.express as px
df = pd.read_csv("data1.csv")
graph1 = px.scatter(df, x = "date", y = "cases", color = "country", title = "Daily Covid Cases")
graph1.show()
