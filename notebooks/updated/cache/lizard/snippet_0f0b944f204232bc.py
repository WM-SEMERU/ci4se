def merge_tracks(self, track_indices=None, mode='sum', program=0, is_drum=
    False, name='merged', remove_merged=False):
    if mode not in ('max', 'sum', 'any'):
        raise ValueError("`mode` must be one of {'max', 'sum', 'any'}.")
    merged = self[track_indices].get_merged_pianoroll(mode)
    merged_track = Track(merged, program, is_drum, name)
    self.append_track(merged_track)
    if remove_merged:
        self.remove_tracks(track_indices)