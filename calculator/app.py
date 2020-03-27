"""
Author:         Chris Unice
Description:    This script controls building and launching the app. All function callbacks
                are contained in this file
"""
# --- Import ---
import dash
from dash.dependencies import Output, Input, State
import locale
import layouts
import functions
from datetime import datetime
import numpy as np

# --- Application set up ---
app = dash.Dash("LODAT")
app.layout = layouts.main_layout()

locale.setlocale(locale.LC_ALL, '')
app_launch_time = datetime.timestamp(datetime.now())


# --- Callbacks ---
@app.callback(
    [
        Output('purchase-price', 'children'),
        Output('down-payment', 'children'),
        Output('principle-interest', 'children'),
        Output('hoa-output', 'children'),
        Output('home-insurance', 'children'),
        Output('property-tax', 'children'),
        Output('mortgage', 'children'),
        Output('cap-ex', 'children'),
        Output('vacancy', 'children'),
        Output('property-mgt', 'children'),
        Output('profit-margin', 'children'),
        Output('required-rent-amount', 'children'),
    ],  # outputs
    [
        Input('calculate-button', 'n_clicks_timestamp'),
        Input('reset-button', 'n_clicks_timestamp')
    ],  # inputs
    [
        State('capital', 'value'),
        State('loan-apr', 'value'),
        State('hoa-input', 'value'),
        State('property-tax-rate', 'value'),
        State('cap-ex-rate', 'value'),
        State('vacancy-rate', 'value'),
        State('property-mgt-rate', 'value'),
        State('desired-profit', 'value'),
        State('desired-profit-radio-items', 'value')
    ]   # states
)
def calculate_button_event(calculate_timestamp, reset_timestamp, capital, apr, hoa, tax_rate,
                           cap_rate, vac_rate, mgt_rate, profit, profit_type):
    # Do nothing if no button has been pushed
    if calculate_timestamp is None and reset_timestamp is None:
        raise dash.exceptions.PreventUpdate
    # Do nothing if there aren't any inputs
    elif None in [capital, apr, hoa, tax_rate, cap_rate, vac_rate, mgt_rate, profit]:
        raise dash.exceptions.PreventUpdate
    # Calculate button has been pushed & Reset button has not
    elif calculate_timestamp is None and reset_timestamp is not None:
        calculate_timestamp = app_launch_time
    # Reset button has been pushed & Calculate button has not
    elif reset_timestamp is None and calculate_timestamp is not None:
        reset_timestamp = app_launch_time
    # Both buttons have been pushed at least once
    elif np.isscalar(calculate_timestamp) and np.isscalar(reset_timestamp):
        pass
    # Catch all
    else:
        raise ValueError('Unhandled button properties {} and {}'.format(calculate_timestamp, reset_timestamp))

    # Calculate button was pushed last
    if calculate_timestamp > reset_timestamp:
        if profit_type == '%':
            profit_is_percent = True
        else:
            profit_is_percent = False
        breakdown = functions.Breakdown(capital, apr, hoa, tax_rate, cap_rate,
                                        vac_rate, mgt_rate, profit, profit_is_percent)
        results = list(map(
            lambda x: locale.currency(x, grouping=True),
            [breakdown.purchase_price, breakdown.down_payment, breakdown.principle_interest,
             breakdown.hoa, breakdown.home_insurance, breakdown.property_tax, breakdown.mortgage,
             breakdown.cap_ex, breakdown.vacancy, breakdown.property_mgt, breakdown.profit_margin,
             breakdown.required_rent]
        ))
        return results
    # Reset button was pushed last
    elif reset_timestamp > calculate_timestamp:
        return ['_'*10 for i in range(12)]


@app.callback(
    [
        Output('capital', 'value'),
        Output('loan-apr', 'value'),
        Output('hoa-input', 'value'),
        Output('property-tax-rate', 'value'),
        Output('cap-ex-rate', 'value'),
        Output('vacancy-rate', 'value'),
        Output('property-mgt-rate', 'value'),
        Output('desired-profit', 'value'),
        Output('calculate-button', 'n_clicks'),
        Output('desired-profit-radio-items', 'value')
    ],  # outputs
    [Input('reset-button', 'n_clicks')]
)
def reset_button_event(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    else:
        return ['' for i in range(8)] + [0, '$']


# --- Main ---
if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=0.1,
        dev_tools_hot_reload_watch_interval=0.1
    )
# end file
