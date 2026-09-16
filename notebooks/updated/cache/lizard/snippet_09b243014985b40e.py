def is_sw_writable(self):
    sw = self.get_property('sw')
    return sw in (rdltypes.AccessType.rw, rdltypes.AccessType.rw1, rdltypes
        .AccessType.w, rdltypes.AccessType.w1)