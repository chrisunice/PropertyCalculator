# --- Import ---
import dash
import locale
import layouts

# --- Application set up ---
app = dash.Dash("LODAT")
# app.scripts.config.serve_locally = True
app.layout = layouts.main_layout()

locale.setlocale(locale.LC_ALL, '')

# --- Callbacks ---
@app.callback(dash.dependencies.Output('purchase-price-input', 'value'),
              [dash.dependencies.Input('capital-input', 'value')])
def update_purchase_price_input(value):
    if value is not None:
        tmp = float(value)/0.2
        return locale.currency(tmp, grouping=True)


@app.callback(dash.dependencies.Output('home-insurance-percent-input', 'value'),
              [dash.dependencies.Input('purchase-price-input', 'value')])
def update_home_insurance_percent_input(value):
    if value is not None:
        my_percent = (1200/456000) * 100
        return round(my_percent, 2)


@app.callback(dash.dependencies.Output('home-insurance-amount-input', 'value'),
              [dash.dependencies.Input('home-insurance-percent-input', 'value')],
              [dash.dependencies.State('purchase-price-input', 'value')])
def update_home_insurance_amount_input(insurance_percent, purchase_price):
    if insurance_percent and purchase_price is not None:
        ip = insurance_percent / 100  # convert to percentage
        pp = float(purchase_price.replace('$', '').replace(',', ''))  # convert string currency to number
        if (ip * pp) < 500:
            tmp = 500 / 12
        else:
            tmp = (ip * pp) / 12
        return locale.currency(tmp, grouping=True)


@app.callback(dash.dependencies.Output('property-tax-amount-input', 'value'),
              [dash.dependencies.Input('property-tax-percent-input', 'value'),
               dash.dependencies.Input('purchase-price-input', 'value')])
def update_property_tax_amount_input(tax_percent, purchase_price):
    if purchase_price and tax_percent is not None:
        tp = tax_percent / 100  # convert to percentage
        pp = float(purchase_price.replace('$', '').replace(',', ''))  # convert string currency to number
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
