def sample_near(self, doc, n_samples=1):
    doc = np.asarray(doc)
    num_features = len(self.kdes_)
    sizes = self.rng_.randint(low=1, high=num_features + 1, size=n_samples)
    samples = []
    for size in sizes:
        to_change = self.rng_.choice(num_features, size, replace=False)
        new_doc = doc.copy()
        for i in to_change:
            kde = self.kdes_[i]
            new_doc[i] = kde.sample(random_state=self.rng_).ravel()
        samples.append(new_doc)
    samples = np.asarray(samples)
    return samples, self._similarity(doc, samples)