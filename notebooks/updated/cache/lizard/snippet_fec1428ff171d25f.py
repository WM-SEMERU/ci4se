def echo_via_pager(text_or_generator, color=None):
    color = resolve_color_default(color)
    if inspect.isgeneratorfunction(text_or_generator):
        i = text_or_generator()
    elif isinstance(text_or_generator, string_types):
        i = [text_or_generator]
    else:
        i = iter(text_or_generator)
    text_generator = (el if isinstance(el, string_types) else text_type(el) for
        el in i)
    from ._termui_impl import pager
    return pager(itertools.chain(text_generator, '\n'), color)