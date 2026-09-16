def _combine_variant_collections(cls, combine_fn, variant_collections, kwargs):
    kwargs['variants'] = combine_fn(*[set(vc) for vc in variant_collections])
    kwargs['source_to_metadata_dict'] = cls._merge_metadata_dictionaries([
        vc.source_to_metadata_dict for vc in variant_collections])
    kwargs['sources'] = set.union(*[vc.sources for vc in variant_collections])
    for key, value in variant_collections[0].to_dict().items():
        if key not in kwargs:
            kwargs[key] = value
    return cls(**kwargs)