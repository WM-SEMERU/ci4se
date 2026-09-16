def _calculate_sunrise_hour_angle(self, solar_dec, depression=0.833):
    hour_angle_arg = math.degrees(math.acos(math.cos(math.radians(90 +
        depression)) / (math.cos(math.radians(self.latitude)) * math.cos(
        math.radians(solar_dec))) - math.tan(math.radians(self.latitude)) *
        math.tan(math.radians(solar_dec))))
    return hour_angle_arg