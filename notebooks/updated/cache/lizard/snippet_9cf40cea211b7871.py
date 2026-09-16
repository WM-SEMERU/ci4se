def loadModel(self, model_file):
    with open(model_file) as f:
        self.q_table = json.load(f)