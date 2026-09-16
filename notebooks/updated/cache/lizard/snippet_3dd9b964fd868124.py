def sample_to_frame_range(self, sample_index):
    start = max(0, int((sample_index - self.frame_size) / self.hop_size) + 1)
    end = int(sample_index / self.hop_size) + 1
    return start, end