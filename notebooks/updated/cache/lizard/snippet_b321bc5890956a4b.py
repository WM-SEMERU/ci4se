def maximal_balanced_subset(self, by_duration=False, label_list_ids=None):
    all_label_values = self.corpus.all_label_values(label_list_ids=
        label_list_ids)
    if by_duration:
        utterance_durations = {utt_idx: utt.duration for utt_idx, utt in
            self.corpus.utterances.items()}
        total_duration_per_label = self.corpus.label_durations(label_list_ids
            =label_list_ids)
        rarest_label_duration = sorted(total_duration_per_label.values())[0]
        target_duration = len(all_label_values) * rarest_label_duration
        label_durations_per_utterance = {}
        for utt_idx, utt in self.corpus.utterances.items():
            label_durations_per_utterance[utt_idx] = utt.label_total_duration(
                label_list_ids)
        subset_utterance_ids = utils.select_balanced_subset(
            label_durations_per_utterance, target_duration, list(
            all_label_values), select_count_values=utterance_durations,
            seed=self.rand.random())
    else:
        total_count_per_label = self.corpus.label_count(label_list_ids=
            label_list_ids)
        lowest_label_count = sorted(total_count_per_label.values())[0]
        target_label_count = lowest_label_count * len(all_label_values)
        utterance_with_label_counts = collections.defaultdict(dict)
        for utterance_idx, utterance in self.corpus.utterances.items():
            utterance_with_label_counts[utterance_idx] = utterance.label_count(
                label_list_ids=label_list_ids)
        subset_utterance_ids = utils.select_balanced_subset(
            utterance_with_label_counts, target_label_count, list(
            all_label_values), seed=self.rand.random())
    filter = subview.MatchingUtteranceIdxFilter(utterance_idxs=set(
        subset_utterance_ids))
    return subview.Subview(self.corpus, filter_criteria=[filter])