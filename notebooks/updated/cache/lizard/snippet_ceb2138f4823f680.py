def _is_good_file_for_multiqc(fpath):
    ftype, encoding = mimetypes.guess_type(fpath)
    if encoding is not None:
        return False
    if ftype is not None and ftype.startswith('image'):
        return False
    return True