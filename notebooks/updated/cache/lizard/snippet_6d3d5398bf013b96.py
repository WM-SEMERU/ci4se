def pretty_dict_str(d, indent=2):
    b = StringIO()
    write_pretty_dict_str(b, d, indent=indent)
    return b.getvalue()