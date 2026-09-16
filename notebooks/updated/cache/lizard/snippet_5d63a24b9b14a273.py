def vtmlrender(vtmarkup, plain=None, strict=False, vtmlparser=VTMLParser()):
    if isinstance(vtmarkup, VTMLBuffer):
        return vtmarkup.plain() if plain else vtmarkup
    try:
        vtmlparser.feed(vtmarkup)
        vtmlparser.close()
    except:
        if strict:
            raise
        buf = VTMLBuffer()
        buf.append_str(str(vtmarkup))
        return buf
    else:
        buf = vtmlparser.getvalue()
        return buf.plain() if plain else buf
    finally:
        vtmlparser.reset()