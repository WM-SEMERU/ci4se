def light_travel_time_to_detector(self, det):
    d = self.location - det.location
    return float(d.dot(d) ** 0.5 / constants.c.value)