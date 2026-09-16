def _get_proc_like_prefix(self, sig):
    sig_match = chpl_sig_pattern.match(sig)
    if sig_match is None:
        return ChapelObject.get_signature_prefix(self, sig)
    prefixes, _, _, _, _ = sig_match.groups()
    if prefixes:
        return prefixes.strip() + ' '
    elif self.objtype.startswith('iter'):
        return 'iter' + ' '
    elif self.objtype in ('method', 'function'):
        return 'proc' + ' '
    else:
        return ChapelObject.get_signature_prefix(self, sig)