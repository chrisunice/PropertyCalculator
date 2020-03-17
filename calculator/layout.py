"""
Author: Chris Unice
Description:    This script is to define all the layouts (pages) that will
                be used by the application.
"""
# --- Imports ---
import dash_html_components as html


# --- Functions (layouts) ---
def main_layout():
    layout = html.Div(
        children=[
            html.Div(
                id='calculator-outline',
                children=[],
                style={
                    'position': 'absolute',
                    'width': '40%',
                    'marginLeft': '30%',
                    'height': '90%',
                    'marginTop': '1%',
                    'backgroundColor': 'lightGrey',
                    'borderStyle': 'outset',
                    'borderWidth': '1.5px',
                    'borderRadius': '15px'
                }
            )
        ]
    )
    return layout
# end file
