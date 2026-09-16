def load_subset(corpus, path, subset_idx):
    csv_file = os.path.join(path, '{}.tsv'.format(subset_idx))
    subset_utt_ids = []
    entries = textfile.read_separated_lines_generator(csv_file, separator=
        '\t', max_columns=8, ignore_lines_starting_with=['client_id'],
        keep_empty=True)
    for entry in entries:
        file_idx = CommonVoiceReader.create_assets_if_needed(corpus, path,
            entry)
        subset_utt_ids.append(file_idx)
    filter = subset.MatchingUtteranceIdxFilter(utterance_idxs=set(
        subset_utt_ids))
    subview = subset.Subview(corpus, filter_criteria=[filter])
    corpus.import_subview(subset_idx, subview)