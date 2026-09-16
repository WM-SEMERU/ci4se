def get_recid_from_ref(ref_obj):
    if not isinstance(ref_obj, dict):
        return None
    url = ref_obj.get('$ref', '')
    return maybe_int(url.split('/')[-1])