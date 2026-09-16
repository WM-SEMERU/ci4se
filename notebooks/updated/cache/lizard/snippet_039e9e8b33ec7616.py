def _handle_tag_csmtextsettings(self):
    obj = _make_object('CSMTextSettings')
    obj.TextId = unpack_ui16(self._src)
    bc = BitConsumer(self._src)
    obj.UseFlashType = bc.u_get(2)
    obj.GridFit = bc.u_get(3)
    obj.Reserved1 = bc.u_get(3)
    obj.Thickness = unpack_float(self._src)
    obj.Sharpness = unpack_float(self._src)
    obj.Reserved2 = unpack_ui8(self._src)
    return obj