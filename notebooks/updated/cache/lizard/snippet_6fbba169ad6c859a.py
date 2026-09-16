def parse_rule(cls, txt):
    types = {'glob': GlobRule, 'regex': RegexRule, 'range': RangeRule,
        'before': TimestampRule, 'after': TimestampRule}
    label, txt = Rule._parse_label(txt)
    if label is None:
        if '*' in txt:
            label = 'glob'
        else:
            label = 'range'
    elif label not in types:
        raise ConfigurationError("'%s' is not a valid package filter type" %
            label)
    rule_cls = types[label]
    txt_ = '%s(%s)' % (label, txt)
    try:
        rule = rule_cls._parse(txt_)
    except Exception as e:
        raise ConfigurationError(
            "Error parsing package filter '%s': %s: %s" % (txt_, e.
            __class__.__name__, str(e)))
    return rule