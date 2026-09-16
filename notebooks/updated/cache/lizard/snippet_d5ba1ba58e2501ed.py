def decrypt_or_cache(filename, **kwargs):
    clear_fname = enc_to_clear_filename(filename)
    if clear_fname:
        return json.load(open(clear_fname))
    return decrypt_file(filename, **kwargs)