def _get_sig_prefix(self, sig):
    if self._is_proc_like():
        return self._get_proc_like_prefix(sig)
    elif self._is_attr_like():
        return self._get_attr_like_prefix(sig)
    else:
        return ChapelObject.get_signature_prefix(self, sig)