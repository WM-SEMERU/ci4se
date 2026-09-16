def contributions(self):
    if self._contributions is None:
        self._contributions = self.contributor.contributions.filter(
            content__published__gte=self.start, content__published__lt=self.end
            )
    return self._contributions