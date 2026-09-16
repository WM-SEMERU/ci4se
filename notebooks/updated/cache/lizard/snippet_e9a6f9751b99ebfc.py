def join_css_class(css_class, *additional_css_classes):
    css_set = set(chain.from_iterable(c.split(' ') for c in [css_class, *
        additional_css_classes] if c))
    return ' '.join(css_set)