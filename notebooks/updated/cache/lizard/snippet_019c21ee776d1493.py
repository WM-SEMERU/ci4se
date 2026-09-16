def run_tracking(self, label_image_1, label_image_2):
    self.scale = self.parameters_tracking['avgCellDiameter'] / 35.0
    detections_1 = self.derive_detections(label_image_1)
    detections_2 = self.derive_detections(label_image_2)
    traces = self.find_initials_traces(detections_1, detections_2)
    for _ in range(int(self.parameters_tracking['iterations'])):
        traces = self.improve_traces(detections_1, detections_2, traces)
    return [(trace.previous_cell.number, trace.current_cell.number) for
        trace in traces]