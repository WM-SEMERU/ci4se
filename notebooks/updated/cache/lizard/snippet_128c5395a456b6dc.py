def load_data_and_labels():
    get_chinese_text()
    positive_examples = list(codecs.open('./data/pos.txt', 'r', 'utf-8').
        readlines())
    positive_examples = [s.strip() for s in positive_examples]
    positive_examples = [pe for pe in positive_examples if len(pe) < 100]
    negative_examples = list(codecs.open('./data/neg.txt', 'r', 'utf-8').
        readlines())
    negative_examples = [s.strip() for s in negative_examples]
    negative_examples = [ne for ne in negative_examples if len(ne) < 100]
    x_text = positive_examples + negative_examples
    x_text = [list(s) for s in x_text]
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]