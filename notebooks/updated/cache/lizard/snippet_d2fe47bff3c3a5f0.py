def fmt_subst(regex, subst):
    return lambda text: re.sub(regex, subst, text) if text else text