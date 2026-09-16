def variants(vcf_fn, region=None, fields=None, exclude_fields=None, dtypes=
    None, arities=None, fills=None, transformers=None, vcf_types=None,
    count=None, progress=0, logstream=None, condition=None, slice_args=None,
    flatten_filter=False, verbose=True, cache=False, cachedir=None,
    skip_cached=False, compress_cache=False, truncate=True):
    loader = _VariantsLoader(vcf_fn, region=region, fields=fields,
        exclude_fields=exclude_fields, dtypes=dtypes, arities=arities,
        fills=fills, transformers=transformers, vcf_types=vcf_types, count=
        count, progress=progress, logstream=logstream, condition=condition,
        slice_args=slice_args, flatten_filter=flatten_filter, verbose=
        verbose, cache=cache, cachedir=cachedir, skip_cached=skip_cached,
        compress_cache=compress_cache, truncate=truncate)
    return loader.load()