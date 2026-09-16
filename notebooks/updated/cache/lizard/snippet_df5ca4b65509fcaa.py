def named_field_regex(keypat_tups):
    keypat_tups_ = [((None, tup) if isinstance(tup, six.string_types) else
        tup) for tup in keypat_tups]
    named_fields = [named_field(key, pat) for key, pat in keypat_tups_]
    regex = ''.join(named_fields)
    return regex