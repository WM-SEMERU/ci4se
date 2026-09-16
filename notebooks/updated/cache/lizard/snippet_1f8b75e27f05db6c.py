def Tag(env, target, source, *more_tags, **kw_tags):
    if not target:
        target = source
        first_tag = None
    else:
        first_tag = source
    if first_tag:
        kw_tags[first_tag[0]] = ''
    if len(kw_tags) == 0 and len(more_tags) == 0:
        raise UserError('No tags given.')
    for x in more_tags:
        kw_tags[x] = ''
    if not SCons.Util.is_List(target):
        target = [target]
    else:
        target = env.Flatten(target)
    for t in target:
        for k, v in kw_tags.items():
            if k[:10] != 'PACKAGING_':
                k = 'PACKAGING_' + k
            t.Tag(k, v)