def get_last_next(self, date):
    past, future = (None, None), (None, None)
    for mjd, value in reversed(self.data):
        if mjd <= date:
            past = mjd, value
            break
        future = mjd, value
    return past, future