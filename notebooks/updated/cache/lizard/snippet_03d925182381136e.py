def read_vocab(args, column_name):
    vocab_path = os.path.join(args.analysis, feature_transforms.
        VOCAB_ANALYSIS_FILE % column_name)
    if not file_io.file_exists(vocab_path):
        return []
    vocab, _ = feature_transforms.read_vocab_file(vocab_path)
    return vocab