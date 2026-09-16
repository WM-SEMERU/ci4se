def badge_color(self):
    if not self.thresholds:
        return self.default_color
    if self.value_type == str:
        if self.value in self.thresholds:
            return self.thresholds[self.value]
        else:
            return self.default_color
    threshold_list = [[self.value_type(i[0]), i[1]] for i in self.
        thresholds.items()]
    threshold_list.sort(key=lambda x: x[0])
    color = None
    for threshold, color in threshold_list:
        if float(self.value) < float(threshold):
            return color
    if color and self.use_max_when_value_exceeds:
        return color
    else:
        return self.default_color