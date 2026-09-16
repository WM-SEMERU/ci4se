def serialize(self, buf, offset):
    fields = [ofproto.oxs_from_user(k, uv) for k, uv in self.fields]
    hdr_pack_str = '!HH'
    field_offset = offset + struct.calcsize(hdr_pack_str)
    for n, value, _ in fields:
        field_offset += ofproto.oxs_serialize(n, value, None, buf, field_offset
            )
    reserved = 0
    length = field_offset - offset
    msg_pack_into(hdr_pack_str, buf, offset, reserved, length)
    self.length = length
    pad_len = utils.round_up(length, 8) - length
    msg_pack_into('%dx' % pad_len, buf, field_offset)
    return length + pad_len