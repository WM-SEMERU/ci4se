def get_nfc_quick_check_property(value, is_bytes=False):
    obj = (unidata.ascii_nfc_quick_check if is_bytes else unidata.
        unicode_nfc_quick_check)
    if value.startswith('^'):
        negated = value[1:]
        value = '^' + unidata.unicode_alias['nfcquickcheck'].get(negated,
            negated)
    else:
        value = unidata.unicode_alias['nfcquickcheck'].get(value, value)
    return obj[value]