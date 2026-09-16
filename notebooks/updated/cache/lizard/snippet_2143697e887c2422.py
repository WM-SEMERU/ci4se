def _find_regular_images(container, contentsinfo):
    for pdfimage, xobj in _image_xobjects(container):
        for draw in contentsinfo.xobject_settings:
            if draw.name != xobj:
                continue
            if draw.stack_depth == 0 and _is_unit_square(draw.shorthand):
                continue
            yield ImageInfo(name=draw.name, pdfimage=pdfimage, shorthand=
                draw.shorthand)