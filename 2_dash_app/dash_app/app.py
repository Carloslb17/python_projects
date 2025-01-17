# dash_app/app.py
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
from db.db_utils import session, SinusoidalData
from predictive_model.model import predict

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Real-Time Dashboard"),
    dcc.Interval(id="interval", interval=1000, n_intervals=0),
    dcc.Graph(id="live-graph"),
])

@app.callback(Output("live-graph", "figure"), [Input("interval", "n_intervals")])
def update_graph(n):
    # Fetch sinusoidal data from the database
    data = session.query(SinusoidalData).all()
    x_values = [d.x for d in data]
    y_values = [d.y for d in data]
    predicted_y = predict(y_values)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode="lines+markers", name="Original"))
    fig.add_trace(go.Scatter(x=x_values, y=predicted_y, mode="lines+markers", name="Predicted"))
    return fig