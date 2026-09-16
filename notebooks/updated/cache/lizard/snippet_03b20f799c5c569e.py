def _process_content_streams(*, pdf, container, shorthand=None):
    if container.get('/Type') == '/Page' and '/Contents' in container:
        initial_shorthand = shorthand or UNIT_SQUARE
    elif container.get('/Type') == '/XObject' and container['/Subtype'
        ] == '/Form':
        ctm = PdfMatrix(shorthand) if shorthand else PdfMatrix.identity()
        form_shorthand = container.get('/Matrix', PdfMatrix.identity())
        form_matrix = PdfMatrix(form_shorthand)
        ctm = form_matrix @ ctm
        initial_shorthand = ctm.shorthand
    else:
        return
    contentsinfo = _interpret_contents(container, initial_shorthand)
    if contentsinfo.found_vector:
        yield VectorInfo()
    yield from _find_inline_images(contentsinfo)
    yield from _find_regular_images(container, contentsinfo)
    yield from _find_form_xobject_images(pdf, container, contentsinfo)