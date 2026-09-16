def js_html(self):
    output = io.StringIO()
    for item in self.js():
        output.write(self.render_asset_html(item, settings.
            CODEMIRROR_JS_ASSET_TAG))
    content = output.getvalue()
    output.close()
    return content