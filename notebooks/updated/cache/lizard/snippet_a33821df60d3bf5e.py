def from_file(fn, **options):
    if hasattr(fn, 'read'):
        return TableFu(fn, **options)
    with open(fn) as f:
        return TableFu(f, **options)