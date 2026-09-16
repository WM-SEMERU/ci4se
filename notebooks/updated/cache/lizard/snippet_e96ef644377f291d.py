def relocate_audio_to_wav_files(self, target_path):
    if not os.path.isdir(target_path):
        os.makedirs(target_path)
    new_tracks = {}
    for track in self.tracks.values():
        track_path = os.path.join(target_path, '{}.wav'.format(track.idx))
        sr = track.sampling_rate
        samples = track.read_samples()
        audio.write_wav(track_path, samples, sr=sr)
        new_track = tracks.FileTrack(track.idx, track_path)
        new_tracks[track.idx] = new_track
    self._tracks = new_tracks
    for utterance in self.utterances.values():
        new_track = self.tracks[utterance.track.idx]
        utterance.track = new_track