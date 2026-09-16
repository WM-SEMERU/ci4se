def _handle_tag_removeobject2(self):
    obj = _make_object('RemoveObject2')
    obj.Depth = unpack_ui16(self._src)
    return obj