def move_editorstack_data(self, start, end):
    if start < 0 or end < 0:
        return
    else:
        steps = abs(end - start)
        direction = (end - start) // steps
    data = self.data
    self.blockSignals(True)
    for i in range(start, end, direction):
        data[i], data[i + direction] = data[i + direction], data[i]
    self.blockSignals(False)
    self.refresh()