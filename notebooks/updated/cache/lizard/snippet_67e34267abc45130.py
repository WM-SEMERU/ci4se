def _merge_meta(left, right, result, clean=True):
    left = BaseSpectrum._get_meta(left)
    right = BaseSpectrum._get_meta(right)
    if clean:
        for key in ('header', 'expr'):
            for d in (left, right):
                if key in d:
                    del d[key]
    mid = metadata.merge(left, right, metadata_conflicts='silent')
    result.meta = metadata.merge(result.meta, mid, metadata_conflicts='silent')