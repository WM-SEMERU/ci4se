def most_similar(self, items, num=10, batch_size=100, show_progressbar=
    False, return_names=True):
    try:
        if items in self.items:
            items = [items]
    except TypeError:
        pass
    x = np.stack([self.norm_vectors[self.items[x]] for x in items])
    result = self._batch(x, batch_size, num + 1, show_progressbar, return_names
        )
    return [x[1:] for x in result]