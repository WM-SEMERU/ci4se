def word_slice(ctx, text, start, stop=0, by_spaces=False):
    text = conversions.to_string(text, ctx)
    start = conversions.to_integer(start, ctx)
    stop = conversions.to_integer(stop, ctx)
    by_spaces = conversions.to_boolean(by_spaces, ctx)
    if start == 0:
        raise ValueError('Start word cannot be zero')
    elif start > 0:
        start -= 1
    if stop == 0:
        stop = None
    elif stop > 0:
        stop -= 1
    words = __get_words(text, by_spaces)
    selection = operator.getitem(words, slice(start, stop))
    return ' '.join(selection)