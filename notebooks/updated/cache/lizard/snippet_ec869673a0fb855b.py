def normalize(self):
    if self.tz is None or timezones.is_utc(self.tz):
        not_null = ~self.isna()
        DAY_NS = ccalendar.DAY_SECONDS * 1000000000
        new_values = self.asi8.copy()
        adjustment = new_values[not_null] % DAY_NS
        new_values[not_null] = new_values[not_null] - adjustment
    else:
        new_values = conversion.normalize_i8_timestamps(self.asi8, self.tz)
    return type(self)._from_sequence(new_values, freq='infer').tz_localize(self
        .tz)