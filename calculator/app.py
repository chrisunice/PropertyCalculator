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

# --- Application set up ---
app = dash.Dash("LODAT")
app.layout = layouts.main_layout()
locale.setlocale(locale.LC_ALL, '')


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
        Input('calculate-button', 'n_clicks'),
        Input('reset-button', 'n_clicks')
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
def calculate_button_event(calculate_event, reset_event, capital, apr, hoa, tax_rate,
                           cap_rate, vac_rate, mgt_rate, profit, profit_type):
    # Waiting for user inputs
    args = [capital, apr, hoa, tax_rate, cap_rate,
            vac_rate, mgt_rate, profit, profit_type]
    if None in args:
        raise dash.exceptions.PreventUpdate

    # Reset outputs
    if reset_event is not None:
        return ['_'*10 for i in range(12)]

    # Populate outputs
    if calculate_event is not None:
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
        Output('desired-profit-radio-items', 'value')
    ],
    [Input('reset-button', 'n_clicks')]
)
def reset_button_event(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    else:
        return [None for i in range(8)] + ['$']


# --- Main ---
if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=0.1,
        dev_tools_hot_reload_watch_interval=0.1
    )
# end file
