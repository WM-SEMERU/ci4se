def add(self, model):
    if isinstance(model, list):
        self.algorithms = self.algorithms + model
    else:
        self.algorithms.append(model)