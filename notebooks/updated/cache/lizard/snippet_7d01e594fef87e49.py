def labels_and_ticks(self):
    labels, idxs = [], []
    for plotter in self.plotters.values():
        sub_labels, sub_idxs, _, _ = plotter.labels_ticks_and_vals()
        labels.append(sub_labels)
        idxs.append(sub_idxs)
    return np.concatenate(labels), np.concatenate(idxs)