def add_hook(self, key_name, hook_name, hook_dict):
    kf = self.dct[key_name]
    if 'hooks' not in kf:
        kf['hooks'] = {}
    kf['hooks'][str(hook_name)] = hook_dict