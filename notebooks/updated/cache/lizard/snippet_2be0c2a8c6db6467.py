def setModel(self, model):
    super(StimulusView, self).setModel(model)
    self.setSelectionModel(ComponentSelectionModel(model))
    self._rects = [([None] * self.model().columnCountForRow(x)) for x in
        range(self.model().rowCount())]
    self._viewIsDirty = True
    self._calculateRects()