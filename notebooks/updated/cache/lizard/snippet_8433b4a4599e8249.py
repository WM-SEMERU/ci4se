def meters(self):
    latitude, longitude = self.latitude_longitude
    meter_x = longitude * ORIGIN_SHIFT / 180.0
    meter_y = math.log(math.tan((90.0 + latitude) * math.pi / 360.0)) / (math
        .pi / 180.0)
    meter_y = meter_y * ORIGIN_SHIFT / 180.0
    return meter_x, meter_y