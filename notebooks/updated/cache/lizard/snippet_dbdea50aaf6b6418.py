def update_thresh(self):
    thresh_val = self.threshLine.value()
    self.threshold_field.setValue(thresh_val)
    self.thresholdUpdated.emit(thresh_val, self.getTitle())