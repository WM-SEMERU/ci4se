def detranslify(in_string):
    try:
        russian = six.text_type(in_string)
    except UnicodeDecodeError:
        raise ValueError('We expects if in_string is 8-bit string,' +
            "then it consists only ASCII chars, but now it doesn't. " +
            'Use unicode in this case.')
    for symb_out, symb_in in TRANSTABLE:
        russian = russian.replace(symb_in, symb_out)
    return russian