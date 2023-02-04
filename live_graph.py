import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen = 5)
X.append(1)

Y = deque(maxlen = 5)
Y.append(1)

Z = deque(maxlen = 5)
Z.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
	[
		dcc.Graph(id = 'live-graph'),
		dcc.Interval(
			id = 'interval-component',
			interval = 1000,
			n_intervals = 1,
		),
	]
)

@app.callback(
	Output('live-graph', 'figure'),
	[ Input('interval-component', 'n_intervals') ]
)
def update_graph_scatter(n):
    Z.append(Z[-1]+Z[-1] * random.uniform(-0.1,0.1))
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    
    fig = go.Figure()
    fig.add_scatter3d(x=list(X), y=list(Y), z=list(Z), uid = 'drone1', mode='lines')
    fig.add_scatter3d(x=list(X), y=list(Y), z=list(Z), uid = 'drone2', mode='lines')

    return fig

if __name__ == '__main__':
	app.run_server(use_reloader=False)
