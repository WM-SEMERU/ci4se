def _filter_attributes(self, keyset):
    filtered = self._filter_keys(self.to_dict(), keyset)
    return Language.make(**filtered)