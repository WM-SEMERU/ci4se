def _load_network(self):
    self.embeddings = load_embeddings(self.lang, type='cw')
    self.model = load_pos_model(lang=self.lang, version=2)

    def predict_proba(input_):
        hidden = np.tanh(np.dot(input_, self.model['W1']) + self.model['b1'])
        output = np.dot(hidden, self.model['W2']) + self.model['b2']
        scores = np.exp(output)
        probs = scores / scores.sum()
        return probs
    return predict_proba