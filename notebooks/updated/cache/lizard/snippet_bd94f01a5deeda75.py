def escape_html(text, escape_slash=False):
    byte_str = text.encode('utf-8')
    ob = lib.hoedown_buffer_new(OUNIT)
    lib.hoedown_escape_html(ob, byte_str, len(byte_str), int(escape_slash))
    try:
        return to_string(ob)
    finally:
        lib.hoedown_buffer_free(ob)