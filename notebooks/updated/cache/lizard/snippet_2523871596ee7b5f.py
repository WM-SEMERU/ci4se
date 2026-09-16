def set_ylabels(self, label=None, **kwargs):
    if label is None:
        label = label_from_attrs(self.data[self._y_var])
    for ax in self._left_axes:
        ax.set_ylabel(label, **kwargs)
    return self