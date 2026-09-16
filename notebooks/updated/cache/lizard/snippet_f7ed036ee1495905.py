def patch_records(diff, from_records, strict=True):
    return patch.apply(diff, from_records, strict=strict)