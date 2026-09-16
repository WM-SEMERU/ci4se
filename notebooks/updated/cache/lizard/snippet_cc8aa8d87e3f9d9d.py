def process_utterance(self, utterance, frame_size=400, hop_size=160, sr=
    None, corpus=None):
    return self.process_track(utterance.track, frame_size=frame_size,
        hop_size=hop_size, sr=sr, start=utterance.start, end=utterance.end,
        utterance=utterance, corpus=corpus)