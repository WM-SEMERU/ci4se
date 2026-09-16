def split_by_proportionally_distribute_labels(self, proportions={},
    use_lengths=True):
    identifiers = {}
    for utterance in self.corpus.utterances.values():
        if use_lengths:
            identifiers[utterance.idx] = {l: int(d * 100) for l, d in
                utterance.label_total_duration().items()}
        else:
            identifiers[utterance.idx] = utterance.label_count()
    splits = utils.get_identifiers_splitted_by_weights(identifiers, proportions
        )
    return self._subviews_from_utterance_splits(splits)