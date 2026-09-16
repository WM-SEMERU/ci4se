def trim_variant_fields(location, ref, alt):
    if len(alt) > 0 and ref.startswith(alt):
        ref = ref[len(alt):]
        location += len(alt)
        alt = ''
    if len(ref) > 0 and alt.startswith(ref):
        alt = alt[len(ref):]
        location += len(ref) - 1
        ref = ''
    return location, ref, alt