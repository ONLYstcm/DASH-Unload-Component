# DASH Unload Component

DASH Unload Component is component which listens to unload event.

Get started with:
1. Install package from local directory (where setup.py is):
    ```
    $ pip install .
    ```
2. Import library and use:
    ```
    import dash_unload_component as duc
    import dash
    from dash.dependencies import Input, Output
    import dash_html_components as html

    app = dash.Dash(__name__)

    app.layout = html.Div([
        duc.Unload(id='page-listener'),
        html.Div(id='listener')
    ])


    @app.callback(Output('listener', 'children'), [Input('page-listener', 'close')])
    def detect_close(close):
        if close is None:
            return None
        print("Current window is closed? ", close)
        return None

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```