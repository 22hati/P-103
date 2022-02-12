import pandas as pd
import plotly.express as px

data_frame = pd.read_csv("data.csv")

print(data_frame)
fig = px.scatter(data_frame, x="date", y="cases", color="country")
fig.show()
