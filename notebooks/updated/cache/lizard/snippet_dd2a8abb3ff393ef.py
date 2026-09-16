def _handle_tag_scriptlimits(self):
    obj = _make_object('ScriptLimits')
    obj.MaxRecursionDepth = unpack_ui16(self._src)
    obj.ScriptTimeoutSeconds = unpack_ui16(self._src)
    return obj