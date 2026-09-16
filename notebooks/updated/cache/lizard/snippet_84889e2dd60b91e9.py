def process_utterance_online(self, utterance, frame_size=400, hop_size=160,
    chunk_size=1, buffer_size=5760000, corpus=None):
    return self.process_track_online(utterance.track, frame_size=frame_size,
        hop_size=hop_size, start=utterance.start, end=utterance.end,
        utterance=utterance, corpus=corpus, chunk_size=chunk_size,
        buffer_size=buffer_size)