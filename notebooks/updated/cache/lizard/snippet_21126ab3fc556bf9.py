def _build_word_co_occurance_graph(self, phrase_list):
    co_occurance_graph = defaultdict(lambda : defaultdict(lambda : 0))
    for phrase in phrase_list:
        for word, coword in product(phrase, phrase):
            co_occurance_graph[word][coword] += 1
    self.degree = defaultdict(lambda : 0)
    for key in co_occurance_graph:
        self.degree[key] = sum(co_occurance_graph[key].values())