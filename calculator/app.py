# --- Import ---
import dash
import layouts

app = dash.Dash("LODAT")
app.layout = layouts.main_layout()

# --- Main ---
if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=0.1,
        dev_tools_hot_reload_watch_interval=0.1
    )
# end file
