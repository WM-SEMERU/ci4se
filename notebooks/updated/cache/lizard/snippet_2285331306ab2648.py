def _get_recording(self, index):
    assert index >= 0
    recs = np.nonzero(index - self.offsets[:-1] >= 0)[0]
    if len(recs) == 0:
        return len(self.arrs) - 1
    return recs[-1]