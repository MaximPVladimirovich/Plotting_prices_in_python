import plotly.express as px
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf


# Load date from csv file
data = pd.read_csv("AAL_data.csv", parse_dates=["date"])

# Set the date column as the index.
data.set_index("date", drop=False, inplace=True)

new_index = pd.date_range(start="2008-05-26", end="2021-04-30", freq="1D")

data = data.reindex(new_index)

data.head()

# # Plot the volum of each using plotly express
# fig = px.line(data, x="date", y="volume", title="Volume of AAL")
# fig.show()


# Plot highest price of each day.
fig = px.line(data, x='date', y="high")
fig.show()





