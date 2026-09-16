def find_cc(arch, args, sp_delta):
    if arch.name not in CC:
        return None
    possible_cc_classes = CC[arch.name]
    for cc_cls in possible_cc_classes:
        if cc_cls._match(arch, args, sp_delta):
            return cc_cls(arch, args=args, sp_delta=sp_delta)
    return None