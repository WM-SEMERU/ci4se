def from_abinit_ixc(cls, ixc):
    ixc = int(ixc)
    if ixc >= 0:
        return cls(**cls.abinitixc_to_libxc[ixc])
    else:
        ixc = abs(ixc)
        first = ixc // 1000
        last = ixc - first * 1000
        x, c = LibxcFunc(int(first)), LibxcFunc(int(last))
        if not x.is_x_kind:
            x, c = c, x
        assert x.is_x_kind and c.is_c_kind
        return cls(x=x, c=c)