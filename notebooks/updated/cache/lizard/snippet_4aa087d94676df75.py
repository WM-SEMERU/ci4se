def import_training_data(self, positive_corpus_file=os.path.join(os.path.
    dirname(__file__), 'positive.txt'), negative_corpus_file=os.path.join(
    os.path.dirname(__file__), 'negative.txt')):
    positive_corpus = open(positive_corpus_file)
    negative_corpus = open(negative_corpus_file)
    positive_training_data = list(map(lambda x: (x, True), positive_corpus))
    negative_training_data = list(map(lambda x: (x, False), negative_corpus))
    self.training_data = positive_training_data + negative_training_data