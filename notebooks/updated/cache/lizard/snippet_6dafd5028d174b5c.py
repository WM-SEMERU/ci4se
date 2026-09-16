def _load_type_counts(self):
    rel_path = os.path.join(CLTK_DATA_DIR, 'old_english', 'model',
        'old_english_models_cltk', 'data', 'oe.counts')
    path = os.path.expanduser(rel_path)
    self.type_counts = {}
    with open(path, 'r') as infile:
        lines = infile.read().splitlines()
        for line in lines:
            count, word = line.split()
            self.type_counts[word] = int(count)