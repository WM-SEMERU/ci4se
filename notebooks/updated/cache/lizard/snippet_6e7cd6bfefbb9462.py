def _figure_data(self, plot, fmt='html', doc=None, as_script=False, **kwargs):
    model = plot.state
    if doc is None:
        doc = plot.document
    else:
        plot.document = doc
    for m in model.references():
        m._document = None
    doc.theme = self.theme
    doc.add_root(model)
    logger = logging.getLogger(bokeh.core.validation.check.__file__)
    logger.disabled = True
    if fmt == 'png':
        from bokeh.io.export import get_screenshot_as_png
        img = get_screenshot_as_png(plot.state, None)
        imgByteArr = BytesIO()
        img.save(imgByteArr, format='PNG')
        data = imgByteArr.getvalue()
        if as_script:
            b64 = base64.b64encode(data).decode('utf-8')
            mime_type, tag = MIME_TYPES[fmt], HTML_TAGS[fmt]
            src = HTML_TAGS['base64'].format(mime_type=mime_type, b64=b64)
            div = tag.format(src=src, mime_type=mime_type, css='')
            js = ''
    else:
        try:
            with silence_warnings(EMPTY_LAYOUT, MISSING_RENDERERS):
                js, div, _ = notebook_content(model)
            html = NOTEBOOK_DIV.format(plot_script=js, plot_div=div)
            data = encode_utf8(html)
            doc.hold()
        except:
            logger.disabled = False
            raise
        logger.disabled = False
    plot.document = doc
    if as_script:
        return div, js
    return data