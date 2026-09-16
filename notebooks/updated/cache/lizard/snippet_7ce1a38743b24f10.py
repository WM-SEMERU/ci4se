def add_swagger(app, json_route, html_route, **kwargs):
    app.route(json_route)(create_swagger_json_handler(app, **kwargs))
    add_swagger_api_route(app, html_route, json_route)