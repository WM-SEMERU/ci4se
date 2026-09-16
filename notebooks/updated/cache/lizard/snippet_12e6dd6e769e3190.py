def render_chart_data(data):
    builder = HtmlBuilder()
    builder._render_objects(data, datatype='chartdata')
    return builder._to_html()