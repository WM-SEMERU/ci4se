def process_corpus_online(self, corpus, output_path, frame_size=400,
    hop_size=160, chunk_size=1, buffer_size=5760000):

    def processing_func(utterance, feat_container, frame_size, hop_size,
        corpus, sr):
        for chunk in self.process_utterance_online(utterance, frame_size=
            frame_size, hop_size=hop_size, corpus=corpus, chunk_size=
            chunk_size, buffer_size=buffer_size):
            feat_container.append(utterance.idx, chunk)
    return self._process_corpus(corpus, output_path, processing_func,
        frame_size=frame_size, hop_size=hop_size, sr=None)