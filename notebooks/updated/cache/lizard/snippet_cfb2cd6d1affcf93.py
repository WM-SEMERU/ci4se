def save(self, model_fname='model.pkl'):
    with open(model_fname, 'wb') as fh:
        pickle.dump(self.stmts, fh, protocol=4)