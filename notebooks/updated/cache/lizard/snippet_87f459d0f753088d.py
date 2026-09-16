def generate_ngram_data_set(self, token_list, n=2):
    n_gram_tuple_zip = self.generate_tuple_zip(token_list, n)
    n_gram_tuple_list = [n_gram_tuple for n_gram_tuple in n_gram_tuple_zip]
    n_gram_data_set = self.generate_tuple_zip(n_gram_tuple_list, 2)
    return n_gram_data_set