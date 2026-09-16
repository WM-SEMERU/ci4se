def match_ref(self, ref):
    if ref in self.refs:
        self._matched_ref = ref
        return True
    return False