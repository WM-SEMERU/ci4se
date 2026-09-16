def tabbed_parsing_character_generator(tmp_dir, train):
    character_vocab = text_encoder.ByteTextEncoder()
    filename = 'parsing_{0}.pairs'.format('train' if train else 'dev')
    pair_filepath = os.path.join(tmp_dir, filename)
    return text_problems.text2text_generate_encoded(text_problems.
        text2text_txt_tab_iterator(pair_filepath), character_vocab)