"""
Author:         Chris Unice
Description:    This script is to define all the layouts (pages) that will
                be used by the application.
"""
# --- Imports ---
import dash_core_components as dcc
import dash_html_components as html


# --- Functions (layouts) ---
def left_column():
    container = html.Div(
        className='left-column',
        children=[
            # CAPITAL SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Capital']
                    ),
                    dcc.Input(
                        id='capital',
                        className='input',
                        type='text',
                        required=True,
                        debounce=True
                    )
                ]
            ),
            html.Hr(),
            # PURCHASE PRICE SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Purchase Price']
                    ),
                    dcc.Input(
                        id='purchase-price',
                        className='input',
                    )
                ]
            ),
            html.Hr(),
            # PRINCIPLE AND INTEREST #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Principle and Interest'],
                    ),
                    dcc.Input(
                        id='principle-interest',
                        className='input',
                    )
                ]
            ),
            html.Hr(),
            # HOME INSURANCE SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Home Insurance']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='home-insurance-amount',
                                className='amount'
                            ),
                            dcc.Input(
                                id='home-insurance-percent',
                                className='percent',
                                readOnly=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # PROPERTY TAX SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Property Tax']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='property-tax-amount',
                                className='amount',
                            ),
                            dcc.Input(
                                id='property-tax-percent',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                                debounce=False,
                                required=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # CAPITAL EXPENDITURE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Capital Expenditure']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='cap-ex-amount',
                                className='amount',
                            ),
                            dcc.Input(
                                id='cap-ex-percent',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                                debounce=False,
                                required=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # VACANCY RATE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Vacancy Rate'],
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='vacancy-rate-amount',
                                className='amount',
                            ),
                            dcc.Input(
                                id='vacancy-rate-percent',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                                debounce=False,
                                required=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # PROPERTY MANAGEMENT #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Property Management']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='property-mgt-amount',
                                className='amount',
                            ),
                            dcc.Input(
                                id='property-mgt-percent',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                                debounce=False,
                                required=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # PROFIT MARGIN #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Profit']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='profit-amount',
                                className='amount',
                            ),
                            dcc.Input(
                                id='profit-percent',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                                debounce=False,
                                required=True
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # REQUIRED RENT #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Rent']
                    ),
                    dcc.Input(
                        className='input',
                        id='rent'
                    )
                ]
            )
        ]
    )
    return container


def main_layout():
    layout = html.Div(
        children=[
            html.Div(
                id='calculator',
                children=[
                    # APP TITLE #
                    html.Div(
                        className='title',
                        children=[
                            html.Label(
                                className='title-text',
                                children=['Investment Calculator']
                            )
                        ]
                    ),
                    # LEFT COLUMN - INPUTS #
                    left_column(),
                ]
            )
        ]
    )
    return layout
# end file
