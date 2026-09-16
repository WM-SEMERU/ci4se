def html(text, extensions=0, render_flags=0):
    extensions = args_to_int(extension_map, extensions)
    render_flags = args_to_int(html_flag_map, render_flags)
    ib = lib.hoedown_buffer_new(IUNIT)
    ob = lib.hoedown_buffer_new(OUNIT)
    renderer = lib.hoedown_html_renderer_new(render_flags, 0)
    document = lib.hoedown_document_new(renderer, extensions, 16)
    lib.hoedown_buffer_puts(ib, text.encode('utf-8'))
    lib.hoedown_document_render(document, ob, ib.data, ib.size)
    lib.hoedown_buffer_free(ib)
    lib.hoedown_document_free(document)
    lib.hoedown_html_renderer_free(renderer)
    try:
        return to_string(ob)
    finally:
        lib.hoedown_buffer_free(ob)