def static_html(self, obj, fmt=None, template=None):
    js_html, css_html = self.html_assets()
    if template is None:
        template = static_template
    html = self.html(obj, fmt)
    return template.format(js=js_html, css=css_html, html=html)