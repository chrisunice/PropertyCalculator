"""
Author: Chris Unice
Description:    This script is to define all the layouts (pages) that will
                be used by the application.
"""
# --- Imports ---
import dash_core_components as dcc
import dash_html_components as html


# --- Functions (layouts) ---
def main_layout():
    layout = html.Div(
        children=[
            html.Div(
                id='calculator-outline',
                className='calculator',
                children=[
                    html.Div(
                        id='capital-container',
                        className='capital',
                        children=[
                            html.Label('Capital'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='down-payment-container',
                        className='down-payment',
                        children=[
                            html.Label('Down Payment'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='property-tax-container',
                        className='property-tax',
                        children=[
                            html.Label('Property Tax'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='home-insurance-container',
                        className='home-insurance',
                        children=[
                            html.Label('Home Insurance'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='capital-expenditure-container',
                        className='capital-expenditure',
                        children=[
                            html.Label('Capital Expenditure'),
                            dcc.Input(),
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='vacancy-rate-container',
                        className='vacancy-rate',
                        children=[
                            html.Label('Vacancy Rate'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='property-mgt-container',
                        className='property-mgt',
                        children=[
                            html.Label('Property Management'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='profit-container',
                        className='profit',
                        children=[
                            html.Label('Profit'),
                            dcc.Input()
                        ]
                    ),
                    html.Hr(),
                    html.Div(
                        id='rent-container',
                        className='rent',
                        children=[
                            html.Label('Rent')
                        ]
                    )
                ]
            )
        ]
    )
    return layout
# end file
