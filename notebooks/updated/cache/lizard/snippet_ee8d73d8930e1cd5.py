def get_collections(self, level, types=None, variables=None, merge=False,
    sampling_rate=None, skip_empty=False, **kwargs):
    from bids.variables import load_variables
    index = load_variables(self, types=types, levels=level, skip_empty=
        skip_empty, **kwargs)
    return index.get_collections(level, variables, merge, sampling_rate=
        sampling_rate)