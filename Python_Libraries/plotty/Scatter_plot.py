import plotly.graph_objs as go
import numpy as np
from plotly.offline import *

N = 1000
first = np.random.rand(N)
second = np.random.rand(N)
trace = go.Scatter(x=first, y=second, mode='markers')
data = [trace]
offline.plot(data)
