def tunable(self, obj):
    self.tune = dict()
    if 'tune' in obj:
        for tunable in MOUNT_TUNABLES:
            tunable_key = tunable[0]
            map_val(self.tune, obj['tune'], tunable_key)
            if tunable_key in self.tune and is_vault_time(self.tune[
                tunable_key]):
                vault_time_s = vault_time_to_s(self.tune[tunable_key])
                self.tune[tunable_key] = vault_time_s
    if 'description' in obj:
        self.tune['description'] = obj['description']