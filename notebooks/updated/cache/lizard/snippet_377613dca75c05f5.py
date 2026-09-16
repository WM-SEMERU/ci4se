def merge_corpus(self, corpus):
    merging_corpus = Corpus.from_corpus(corpus)
    self.import_tracks(corpus.tracks.values())
    self.import_issuers(corpus.issuers.values())
    utterance_idx_mapping = self.import_utterances(corpus.utterances.values())
    for subview_idx, subview in merging_corpus.subviews.items():
        for filter in subview.filter_criteria:
            if isinstance(filter, subset.MatchingUtteranceIdxFilter):
                new_filtered_utt_ids = set()
                for utt_idx in filter.utterance_idxs:
                    new_filtered_utt_ids.add(utterance_idx_mapping[utt_idx].idx
                        )
                filter.utterance_idxs = new_filtered_utt_ids
        new_idx = naming.index_name_if_in_list(subview_idx, self.subviews.
            keys())
        self.import_subview(new_idx, subview)
    for feat_container_idx, feat_container in merging_corpus.feature_containers.items(
        ):
        self.new_feature_container(feat_container_idx, feat_container.path)