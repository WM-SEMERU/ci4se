def merge_cameras(self):
    combined = CaseInsensitiveDict({})
    for sync in self.sync:
        combined = merge_dicts(combined, self.sync[sync].cameras)
    return combined