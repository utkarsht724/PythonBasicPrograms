import plotly.graph_objs as go
import numpy as np
from plotly.offline import *

N = 500
first = np.random.rand(N)
second = np.random.rand(N)
trace = go.Scatter(x=first, y=second, mode='markers',textfont=dict(size=25),)
data = [trace]
offline.plot(data)
