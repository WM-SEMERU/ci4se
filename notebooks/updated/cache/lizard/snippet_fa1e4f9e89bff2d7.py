def b6_evalue_filter(handle, e_value, *args, **kwargs):
    for entry in b6_iter(handle, *args, **kwargs):
        if entry.evalue <= e_value:
            yield entry