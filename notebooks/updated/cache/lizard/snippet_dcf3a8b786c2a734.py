def get_std_start_date(self):
    first, _ = self._val
    if first != datetime.min and first != datetime.max:
        return first.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return ''