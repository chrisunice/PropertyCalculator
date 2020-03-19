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
                id='calculator',
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
                                id='capital-input',
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
                                id='purchase-price-input',
                                className='input',
                                type='text'
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
                                className='input',
                                children=[
                                    dcc.Input(
                                        id='property-tax-amount-input',
                                        className='amount'
                                    ),
                                    dcc.Input(
                                        id='property-tax-percent-input',
                                        className='percent',
                                        placeholder='%',
                                        type='number',
                                        debounce=True
                                    )
                                ]
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
                                className='input',
                                children=[
                                    dcc.Input(
                                        id='home-insurance-amount-input',
                                        className='amount'
                                    ),
                                    dcc.Input(
                                        id='home-insurance-percent-input',
                                        className='percent',
                                        placeholder='%'
                                    )
                                ]
                            )
                        ]
                    ),
                    # html.Hr(),
                    # html.Div(
                    #     id='capital-expenditure-container',
                    #     className='capital-expenditure',
                    #     children=[
                    #         html.Label('Capital Expenditure'),
                    #         dcc.Input(),
                    #     ]
                    # ),
                    # html.Hr(),
                    # html.Div(
                    #     id='vacancy-rate-container',
                    #     className='vacancy-rate',
                    #     children=[
                    #         html.Label('Vacancy Rate'),
                    #         dcc.Input()
                    #     ]
                    # ),
                    # html.Hr(),
                    # html.Div(
                    #     id='property-mgt-container',
                    #     className='property-mgt',
                    #     children=[
                    #         html.Label('Property Management'),
                    #         dcc.Input()
                    #     ]
                    # ),
                    # html.Hr(),
                    # html.Div(
                    #     id='profit-container',
                    #     className='profit',
                    #     children=[
                    #         html.Label('Profit'),
                    #         dcc.Input()
                    #     ]
                    # ),
                    # html.Hr(),
                    # html.Div(
                    #     id='rent-container',
                    #     className='rent',
                    #     children=[
                    #         html.Label('Rent')
                    #     ]
                    # )
                ]
            )
        ]
    )
    return layout
# end file
