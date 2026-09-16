def get_std_end_date(self):
    _, second = self._val
    if second != datetime.max:
        return second.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return ''