def vectorize_dialogues(self, dialogues):
    return np.array([self.vectorize_dialogue(d) for d in dialogues])