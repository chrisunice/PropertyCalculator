# --- Import ---
import dash
import locale
import layouts
import functions
import numpy as np

# --- Application set up ---
app = dash.Dash("LODAT")
app.layout = layouts.main_layout()
locale.setlocale(locale.LC_ALL, '')


# --- Callbacks ---
@app.callback(dash.dependencies.Output('purchase-price', 'children'),
              [dash.dependencies.Input('capital', 'value')])
def update_purchase_price(capital):
    print(capital)
    if capital is None or capital == '':
        raise dash.exceptions.PreventUpdate
    else:
        result = float(capital)/0.2

    return locale.currency(result, grouping=True)

# @app.callback([dash.dependencies.Output('purchase-price', 'value'),
#                dash.dependencies.Output('principle-interest', 'value'),
#                dash.dependencies.Output('home-insurance-percent', 'value'),
#                dash.dependencies.Output('home-insurance-amount', 'value')],
#               [dash.dependencies.Input('capital', 'value')])
# def update_from_capital(capital):
#     if capital is None:
#         raise dash.exceptions.PreventUpdate
#     else:
#         capital = float(capital)
#
#     # Purchase price
#     purchase_price = locale.currency(capital/0.2, grouping=True)
#     # Principle and interest
#     rate = 0.05/12
#     period = 30*12
#     payment = -1 * np.pmt(rate, period, capital*4)
#     payment = locale.currency(payment, grouping=True)
#     # Home insurance percent
#     insurance_percent = np.round(
#         ((1200 / 456000) * 100), 2
#     )
#     # Home insurance amount
#     if (insurance_percent/100 * capital/0.2) < 500:
#         insurance_amount = locale.currency(500/12, grouping=True)
#     else:
#         insurance_amount = locale.currency((insurance_percent/100 * capital/0.2)/12, grouping=True)
#
#     return purchase_price, payment, insurance_percent, insurance_amount
#
#
# @app.callback(dash.dependencies.Output('property-tax-amount', 'value'),
#               [dash.dependencies.Input('property-tax-percent', 'value'),
#                dash.dependencies.Input('purchase-price', 'value')])
# def update_property_tax_amount(tax_percent, purchase_price):
#     if purchase_price and tax_percent is not None:
#         tp = tax_percent / 100  # convert to percentage
#         pp = functions.format2number(purchase_price)  # convert string currency to number
#         tmp = (pp * tp) / 12
#         return locale.currency(tmp, grouping=True)
#
#
# @app.callback([dash.dependencies.Output('cap-ex-amount', 'value'),
#                dash.dependencies.Output('vacancy-rate-amount', 'value'),
#                dash.dependencies.Output('property-mgt-amount', 'value'),
#                dash.dependencies.Output('profit-amount', 'value'),
#                dash.dependencies.Output('rent', 'value')],
#               [dash.dependencies.Input('capital', 'value'),
#                dash.dependencies.Input('property-tax-percent', 'value'),
#                dash.dependencies.Input('cap-ex-percent', 'value'),
#                dash.dependencies.Input('vacancy-rate-percent', 'value'),
#                dash.dependencies.Input('property-mgt-percent', 'value'),
#                dash.dependencies.Input('profit-percent', 'value')])
# def update_rent(capital, tax, cap, vac, mgt, profit):
#     inputs = [capital, tax, cap, vac, mgt, profit]
#     if None in inputs:
#         raise dash.exceptions.PreventUpdate
#     else:
#         capital = float(capital)
#
#     numbers = functions.calculate_breakdown(capital, tax, cap, vac, mgt, profit)
#     currency = map(
#         lambda x: locale.currency(x, grouping=True),
#         numbers
#     )
#     return list(currency)


# --- Main ---
if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=0.1,
        dev_tools_hot_reload_watch_interval=0.1
    )
# end file
