import dash_bootstrap_components as dbc
from dash import Dash
from Data import Data
from Layout import AppLayout
import pandas as pd
from AppCallback import AppCallback



styles = [dbc.themes.BOOTSTRAP]
app = Dash(name = __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=styles)
app.title = "Dashboard"
server = app.server


data = Data()  # here we initionlize Data class object
layout = AppLayout()
app.layout = layout.getAppLayout()
AppCallback(app, data)


if __name__ == "__main__":
    app.run_server(debug=False)