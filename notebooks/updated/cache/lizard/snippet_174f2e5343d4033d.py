def setup(app):
    app.add_node(bokehjs_content, html=(html_visit_bokehjs_content,
        html_depart_bokehjs_content))
    app.add_directive('bokehjs-content', BokehJSContent)