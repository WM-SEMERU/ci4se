def time_at_elevation(self, elevation, direction=SUN_RISING, date=None,
    local=True):
    if local and self.timezone is None:
        raise ValueError(
            'Local time requested but Location has no timezone set.')
    if self.astral is None:
        self.astral = Astral()
    if date is None:
        date = datetime.date.today()
    if elevation > 90.0:
        elevation = 180.0 - elevation
        direction = SUN_SETTING
    time_ = self.astral.time_at_elevation_utc(elevation, direction, date,
        self.latitude, self.longitude)
    if local:
        return time_.astimezone(self.tz)
    else:
        return time_