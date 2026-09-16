def _load_data():
    data = {}
    for name, file_name in (('words', 'hanzi_pinyin_words.tsv'), (
        'characters', 'hanzi_pinyin_characters.tsv')):
        lines = [line.split('\t') for line in dragonmapper.data.
            load_data_file(file_name)]
        data[name] = {hanzi: pinyin.split('/') for hanzi, pinyin in lines}
    return data