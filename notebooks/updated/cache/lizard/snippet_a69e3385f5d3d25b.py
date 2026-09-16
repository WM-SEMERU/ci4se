def configure_installation_source(source_plus_key):
    if source_plus_key.startswith('snap'):
        return
    source, key = get_source_and_pgp_key(source_plus_key)
    try:
        fetch_add_source(source, key, fail_invalid=True)
    except SourceConfigError as se:
        error_out(str(se))