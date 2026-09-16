def get_active_pitch_range(self):
    if self.pianoroll.shape[1] < 1:
        raise ValueError(
            'Cannot compute the active pitch range for an empty pianoroll')
    lowest = 0
    highest = 127
    while lowest < highest:
        if np.any(self.pianoroll[:, (lowest)]):
            break
        lowest += 1
    if lowest == highest:
        raise ValueError(
            'Cannot compute the active pitch range for an empty pianoroll')
    while not np.any(self.pianoroll[:, (highest)]):
        highest -= 1
    return lowest, highest