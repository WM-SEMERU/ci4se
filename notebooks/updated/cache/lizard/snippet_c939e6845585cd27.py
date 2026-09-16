def sort(self):
    self.detections = sorted(self.detections, key=lambda d: d.detect_time)
    return self