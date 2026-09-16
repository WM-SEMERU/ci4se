def stack_suffix(self, context_sensitivity_level):
    ret = ()
    for frame in self:
        if len(ret) >= context_sensitivity_level * 2:
            break
        ret = (frame.call_site_addr, frame.func_addr) + ret
    while len(ret) < context_sensitivity_level * 2:
        ret = (None, None) + ret
    return ret