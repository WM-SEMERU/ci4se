def matches(self, spec):
    if callable(spec) and not isinstance(spec, type):
        return spec(self)
    elif isinstance(spec, type):
        return isinstance(self, spec)
    specification = self.__class__.__name__, self.group, self.label
    split_spec = tuple(spec.split('.')) if not isinstance(spec, tuple
        ) else spec
    split_spec, nocompare = zip(*((None, True) if s == '*' or s is None else
        (s, False) for s in split_spec))
    if all(nocompare):
        return True
    match_fn = itemgetter(*(idx for idx, nc in enumerate(nocompare) if not nc))
    self_spec = match_fn(split_spec)
    unescaped_match = match_fn(specification[:len(split_spec)]) == self_spec
    if unescaped_match:
        return True
    sanitizers = [util.sanitize_identifier, util.group_sanitizer, util.
        label_sanitizer]
    identifier_specification = tuple(fn(ident, escape=False) for ident, fn in
        zip(specification, sanitizers))
    identifier_match = match_fn(identifier_specification[:len(split_spec)]
        ) == self_spec
    return identifier_match