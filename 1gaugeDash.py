import pandas as pd
import csv
import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.plotly as py
import random
import plotly.graph_objs as go
from collections import deque

#with open("aqua.csv", "r") as f:
#       temp_last_line = f.readlines()[-1].strip().split(",")
       #temp_secondlast_line = f.readlines()[-2].strip().split(",")
#X = deque(maxlen=100)
#X.append(temp_last_line)
#X.append(temp_last_line)
Y = deque(maxlen=100)
Y.append("0")
Y.append("0")

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=False),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
     	with open("aqua.csv", "r") as f:
         	last_line = f.readlines()[-1].strip().split(",")
#    	if  str(X[-1]) == str(last_line[1]):
#    	        print("same shit")
#    	else: 
#    	    	X.append(last_line[1])
         	Y.append(last_line[2])
#        	print(X)
        
        fig = go.Figure()
	fig.add_barpolar(r = [1, 1, 1, 1, 1],
                 theta = [0, 36, 72, 108, 144],
                 offset=0,
                 width=36,
                 marker={'color': [0, 1, 2, 3, 4]})

# Configure polar 1
	fig.layout.polar.hole = 0.4
	fig.layout.polar.angularaxis.showgrid = False
	fig.layout.polar.radialaxis.showgrid = False
	fig.layout.polar.radialaxis.range = [0, 1]
	fig.layout.polar.radialaxis.tickvals = []
	fig.layout.polar.bargap = 0.9
	fig.layout.polar.sector = [0, 180]
	fig.layout.polar.domain.x = [0, 1]
	fig

        needle = fig.add_scatterpolar(r=[1, 0, 0, 1],
                              theta=[0, -20, 20, 0],
                              fill='tonext',
                              mode='lines',
                              subplot = 'polar2')
# Configure polar 2 for needle
	fig.layout.polar2 = {}
	fig.layout.polar2.hole = 0.1
	fig.layout.polar2.angularaxis.showgrid = False
	fig.layout.polar2.radialaxis.showgrid = False
	fig.layout.polar2.radialaxis.range = [0, 1]
	fig.layout.polar2.radialaxis.tickvals = []
	fig.layout.polar2.bargap = 0.9
	fig.layout.polar2.sector = [0, 180]
	fig.layout.polar2.domain.x = [0, 1]
	fig.layout.polar2.domain.y = [0, 0.35]
	fig.layout.polar2.angularaxis.tickvals = []		
	fig.layout.polar2.radialaxis.tickvals = []
	fig.layout.polar2.angularaxis.showline = False
	fig.layout.polar2.radialaxis.showline = False 
	Z = float(Y[-1])
        fig.layout.polar2.angularaxis.rotation = int(Z)
       
        
        return {"data": fig.data,"layout": fig.layout}



if __name__ == '__main__':
    app.run_server(debug=True)


