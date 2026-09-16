def result(self):
    if self.subplots:
        if self.layout is not None and not is_list_like(self.ax):
            return self.axes.reshape(*self.layout)
        else:
            return self.axes
    else:
        sec_true = isinstance(self.secondary_y, bool) and self.secondary_y
        all_sec = is_list_like(self.secondary_y) and len(self.secondary_y
            ) == self.nseries
        if sec_true or all_sec:
            return self._get_ax_layer(self.axes[0], primary=False)
        else:
            return self.axes[0]