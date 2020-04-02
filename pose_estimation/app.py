import dash
from scripts.layout import app_layout
from scripts.callbacks import run

# --- Initialize Dash App ---
app = dash.Dash(__name__)
server = app.server
app.title = "Target Pose Estimation"
app.layout = app_layout()

# -- Callbacks ---
_ = run(app)

# --- Main ---
if __name__ == "__main__":
    app.run_server(port=8010,
                   debug=True,
                   dev_tools_hot_reload=True,
                   dev_tools_hot_reload_interval=0.1,
                   dev_tools_hot_reload_watch_interval=0.1)
# end file
