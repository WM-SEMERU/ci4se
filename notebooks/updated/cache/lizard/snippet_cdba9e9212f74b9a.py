def _add_timedelta(self, delta):
    if isinstance(delta, pendulum.Duration):
        return self.add(years=delta.years, months=delta.months, weeks=delta
            .weeks, days=delta.remaining_days)
    return self.add(days=delta.days)