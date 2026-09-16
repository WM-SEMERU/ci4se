def _handle_tag_enabledebugger2(self):
    obj = _make_object('EnableDebugger2')
    obj.Reserved = unpack_ui16(self._src)
    obj.Password = self._get_struct_string()
    return obj