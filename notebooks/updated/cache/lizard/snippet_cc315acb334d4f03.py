def from_notebook_node(self, nb, resources=None, **kw):
    from weasyprint import HTML, CSS
    nb = copy.deepcopy(nb)
    output, resources = super(OneCodexPDFExporter, self).from_notebook_node(nb,
        resources=resources, **kw)
    buf = BytesIO()
    HTML(string=output).write_pdf(buf, stylesheets=[CSS(os.path.join(
        ASSETS_PATH, CSS_TEMPLATE_FILE))])
    buf.seek(0)
    return buf.read(), resources