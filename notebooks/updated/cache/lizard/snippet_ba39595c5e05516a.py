def hacking_localization_strings(logical_line, tokens, noqa):
    r
    if noqa:
        return
    gen = check_i18n()
    next(gen)
    try:
        list(map(gen.send, tokens))
        gen.close()
    except LocalizationError as e:
        yield e.args