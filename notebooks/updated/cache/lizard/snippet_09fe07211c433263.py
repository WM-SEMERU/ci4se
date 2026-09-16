def get_or_create_vocab(self, data_dir, tmp_dir, force_get=False):
    vocab_filepath = os.path.join(data_dir, self.vocab_filename)
    encoder = text_encoder.SubwordTextEncoder(vocab_filepath)
    return encoder