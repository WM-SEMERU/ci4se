def _RegisterKeyFlagForModule(self, module_name, flag):
    key_flags_by_module = self.KeyFlagsByModuleDict()
    key_flags = key_flags_by_module.setdefault(module_name, [])
    if flag not in key_flags:
        key_flags.append(flag)