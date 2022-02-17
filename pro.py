import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("pro.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist = False)
fig.show()
