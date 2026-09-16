def _suggest_semantic_version(s):
    result = s.strip().lower()
    for pat, repl in _REPLACEMENTS:
        result = pat.sub(repl, result)
    if not result:
        result = '0.0.0'
    m = _NUMERIC_PREFIX.match(result)
    if not m:
        prefix = '0.0.0'
        suffix = result
    else:
        prefix = m.groups()[0].split('.')
        prefix = [int(i) for i in prefix]
        while len(prefix) < 3:
            prefix.append(0)
        if len(prefix) == 3:
            suffix = result[m.end():]
        else:
            suffix = '.'.join([str(i) for i in prefix[3:]]) + result[m.end():]
            prefix = prefix[:3]
        prefix = '.'.join([str(i) for i in prefix])
        suffix = suffix.strip()
    if suffix:
        for pat, repl in _SUFFIX_REPLACEMENTS:
            suffix = pat.sub(repl, suffix)
    if not suffix:
        result = prefix
    else:
        sep = '-' if 'dev' in suffix else '+'
        result = prefix + sep + suffix
    if not is_semver(result):
        result = None
    return result