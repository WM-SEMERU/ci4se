def translate(usercodes, rgb_mode=False):
    for code in usercodes:
        code = code.strip().lower()
        if code.isalpha() and code in codes['fore']:
            yield translate_basic(code)
        else:
            if ',' in code:
                try:
                    r, g, b = (int(c.strip()) for c in code.split(','))
                except (TypeError, ValueError):
                    raise InvalidColr(code)
                code = r, g, b
            colorcode = ColorCode(code, rgb_mode=rgb_mode)
            if disabled():
                yield str(colorcode)
            yield colorcode.example()