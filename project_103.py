import pandas as pd
import plotly.express as px

data_read = pd.read_csv('covid.csv')
chart = px.scatter(data_read , x = 'date' , y = 'cases' , color = 'country')
chart.show()
