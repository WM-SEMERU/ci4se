def _supported_imts(self):
    imt_list = []
    for key in self.imls:
        if 'SA' in key:
            imt_list.append(imt_module.SA)
        elif key == 'T':
            continue
        else:
            try:
                factory = getattr(imt_module, key)
            except Exception:
                continue
            imt_list.append(factory)
    return imt_list