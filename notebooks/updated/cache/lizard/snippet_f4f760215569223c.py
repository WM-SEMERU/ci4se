def for_json(self):
    value = super(DatetimeField, self).for_json()
    if isinstance(value, pendulum.Interval):
        return value.in_seconds() * 1000
    if isinstance(value, datetime):
        return self.format_datetime(value)
    if isinstance(value, pendulum.Time):
        return str(value)
    if isinstance(value, pendulum.Date):
        return value.to_date_string()