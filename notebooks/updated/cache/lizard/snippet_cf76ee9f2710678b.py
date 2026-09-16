def _get_struct_rect(self):
    bc = BitConsumer(self._src)
    nbits = bc.u_get(5)
    if self._read_twips:
        return tuple(bc.s_get(nbits) for _ in range(4))
    else:
        return tuple(bc.s_get(nbits) / 20.0 for _ in range(4))