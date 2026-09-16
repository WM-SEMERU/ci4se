def draw_stacked_bar(self, nan_col_counts):
    for index, nan_values in enumerate(nan_col_counts):
        label, nan_col_counts = nan_values
        if index == 0:
            bottom_chart = np.zeros(nan_col_counts.shape)
        if self.classes_ is not None:
            label = self.classes_[index]
        color = self.colors[index]
        self.ax.barh(self.ind - self.width / 2, nan_col_counts, self.width,
            color=color, label=label, left=bottom_chart)
        bottom_chart = nan_col_counts