def Y_tighter(self):
    self.parent.value('y_distance', self.parent.value('y_distance') / 1.4)
    self.parent.traces.display()