def _get_relative_ext(of, sf):

    def half_finished_trim(orig, prefix):
        return os.path.basename(prefix).count('.') > 0 and os.path.basename(
            orig).count('.') == os.path.basename(prefix).count('.')
    if of.find(':') > 0:
        of = os.path.basename(of.split(':')[-1])
    if sf.find(':') > 0:
        sf = os.path.basename(sf.split(':')[-1])
    prefix = os.path.commonprefix([sf, of])
    while prefix.endswith('.') or half_finished_trim(sf, prefix
        ) and half_finished_trim(of, prefix):
        prefix = prefix[:-1]
    exts_to_remove = of.replace(prefix, '')
    ext_to_add = sf.replace(prefix, '')
    if not exts_to_remove or exts_to_remove.startswith('.'):
        return str('^' * exts_to_remove.count('.') + ext_to_add)
    else:
        raise ValueError(
            'No cross platform way to reference complex extension: %s %s' %
            (sf, of))