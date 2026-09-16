def load_model(self, path):
    with open(path, 'rb') as in_file:
        self.__dict__.update(dill.load(in_file).__dict__)