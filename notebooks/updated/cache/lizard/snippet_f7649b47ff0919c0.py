def get_sample_frame(self):
    for frame in self.frames:
        return frame.open()
    for res in self.results.values():
        return res.open()
    return None