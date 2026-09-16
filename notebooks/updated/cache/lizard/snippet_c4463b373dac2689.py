def classifier(self):
    clf = pickle.load(open(os.path.join(self.repopath, 'classifier.pkl')))
    return clf