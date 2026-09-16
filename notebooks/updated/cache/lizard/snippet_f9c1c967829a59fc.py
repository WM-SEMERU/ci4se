def register_layouts(layouts, app, url='/api/props/', brand='Pyxley'):

    def props(name):
        if name not in layouts:
            name = list(layouts.keys())[0]
        return jsonify({'layouts': layouts[name]['layout']})

    def apps():
        paths = []
        for i, k in enumerate(layouts.keys()):
            if i == 0:
                paths.append({'path': '/', 'label': layouts[k].get('title', k)}
                    )
            paths.append({'path': '/' + k, 'label': layouts[k].get('title', k)}
                )
        return jsonify({'brand': brand, 'navlinks': paths})
    app.add_url_rule(url + '<string:name>/', view_func=props)
    app.add_url_rule(url, view_func=apps)