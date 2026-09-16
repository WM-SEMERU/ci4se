def tabbed_parsing_token_generator(data_dir, tmp_dir, train, prefix,
    source_vocab_size, target_vocab_size):
    filename = 'parsing_{0}.pairs'.format('train' if train else 'dev')
    source_vocab = generator_utils.get_or_generate_tabbed_vocab(data_dir,
        tmp_dir, filename, 0, prefix + '_source.tokens.vocab.%d' %
        source_vocab_size, source_vocab_size)
    target_vocab = generator_utils.get_or_generate_tabbed_vocab(data_dir,
        tmp_dir, filename, 1, prefix + '_target.tokens.vocab.%d' %
        target_vocab_size, target_vocab_size)
    pair_filepath = os.path.join(tmp_dir, filename)
    return text_problems.text2text_generate_encoded(text_problems.
        text2text_txt_tab_iterator(pair_filepath), source_vocab, target_vocab)