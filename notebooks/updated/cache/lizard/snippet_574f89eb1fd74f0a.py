def import_ed25519_publickey_from_file(filepath):
    securesystemslib.formats.PATH_SCHEMA.check_match(filepath)
    ed25519_key_metadata = securesystemslib.util.load_json_file(filepath)
    ed25519_key, junk = securesystemslib.keys.format_metadata_to_key(
        ed25519_key_metadata)
    if ed25519_key['keytype'] != 'ed25519':
        message = 'Invalid key type loaded: ' + repr(ed25519_key['keytype'])
        raise securesystemslib.exceptions.FormatError(message)
    return ed25519_key