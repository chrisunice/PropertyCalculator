# --- Import ---
import dash
from layout import main_layout


# --- Main ---
if __name__ == "__main__":
    app = dash.Dash("LODAT")
    app.layout = main_layout()
    app.run_server(debug=True)
# end file
