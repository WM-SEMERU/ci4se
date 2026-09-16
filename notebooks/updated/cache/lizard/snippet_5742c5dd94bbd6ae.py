def biclique_size(self, xmin, xmax, ymin, ymax):
    try:
        return self._biclique_size[xmin, xmax, ymin, ymax]
    except KeyError:
        hscore = self.hline_score(ymin, xmin, xmax)
        vscore = self.vline_score(xmin, ymin, ymax)
        if ymin < ymax:
            hscore += self.biclique_size(xmin, xmax, ymin + 1, ymax)[0]
        if xmin < xmax:
            vscore += self.biclique_size(xmin + 1, xmax, ymin, ymax)[1]
        self._biclique_size[xmin, xmax, ymin, ymax] = hscore, vscore
        return hscore, vscore