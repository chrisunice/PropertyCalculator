# --- Import ---
import dash
import locale
import layouts

# --- Application set up ---
app = dash.Dash("LODAT")
app.layout = layouts.main_layout()

locale.setlocale(locale.LC_ALL, '')

# --- Callbacks ---
# @app.callback(dash.dependencies.Output('capital-input', 'value'),
#               [dash.dependencies.Input('capital-input', 'value')])
# def update_capital_input_format(value):
#     if value is not None:
#         return locale.currency(value, grouping=True)

@app.callback(dash.dependencies.Output('purchase-price-input', 'value'),
              [dash.dependencies.Input('capital-input', 'value')])
def update_purchase_price_input(value):
    if value is not None:
        tmp = float(value)/0.2
        return locale.currency(tmp, grouping=True)


@app.callback(dash.dependencies.Output('property-tax-amount-input', 'value'),
              [dash.dependencies.Input('purchase-price-input', 'value'),
               dash.dependencies.Input('property-tax-percent-input', 'value')])
def update_property_tax_amount_input(purchase_price, tax_percent):
    if purchase_price and tax_percent is not None:
        pp = float(purchase_price.replace('$', '').replace(',', ''))  # convert string currency
        tp = tax_percent / 100  # convert to percentage
        # TODO add check for tax percent is between 0 and 100
        tmp = (pp * tp) / 12
        return locale.currency(tmp, grouping=True)


# --- Main ---
if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=0.1,
        dev_tools_hot_reload_watch_interval=0.1
    )
# end file
