def draw(self, **kwargs):
    colors = resolve_colors(n_colors=len(self.pos_tag_counts_), colormap=
        self.colormap, colors=self.colors)
    if self.frequency:
        sorted_tags = sorted(self.pos_tag_counts_, key=self.pos_tag_counts_
            .get, reverse=True)
        sorted_counts = [self.pos_tag_counts_[tag] for tag in sorted_tags]
        self.ax.bar(range(len(sorted_tags)), sorted_counts, color=colors)
        return self.ax
    self.ax.bar(range(len(self.pos_tag_counts_)), list(self.pos_tag_counts_
        .values()), color=colors)
    return self.ax