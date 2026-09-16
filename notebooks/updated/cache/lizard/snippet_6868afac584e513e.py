def has_source_contents(self, src_id):
    return bool(rustcall(_lib.lsm_view_has_source_contents, self._get_ptr(),
        src_id))