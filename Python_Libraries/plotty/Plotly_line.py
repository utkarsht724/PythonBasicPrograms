import plotly.graph_objs as go
import numpy as np

N = 100
random_x = np.linspace(0, 1, N)

random_y= np.random.randn(N)

fig = go.Figure()

fig.add_trace(go.Scatter(x=random_x, y=random_y,mode='lines',name='lines'))

fig.show()