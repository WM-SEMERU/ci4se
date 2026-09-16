def is_too_early_to_signup(self, now=None):
    if now is None:
        now = datetime.datetime.now()
    activity_date = datetime.datetime.combine(self.block.date, datetime.
        time(0, 0, 0))
    presign_period = datetime.timedelta(days=2)
    return now < activity_date - presign_period