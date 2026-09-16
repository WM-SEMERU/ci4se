def _expand(template, seq):
    if is_text(template):
        return _simple_expand(template, seq)
    elif is_data(template):
        template = wrap(template)
        assert template['from'], "Expecting template to have 'from' attribute"
        assert template.template, "Expecting template to have 'template' attribute"
        data = seq[-1][template['from']]
        output = []
        for d in data:
            s = seq + (d,)
            output.append(_expand(template.template, s))
        return coalesce(template.separator, '').join(output)
    elif is_list(template):
        return ''.join(_expand(t, seq) for t in template)
    else:
        if not _Log:
            _late_import()
        _Log.error('can not handle')