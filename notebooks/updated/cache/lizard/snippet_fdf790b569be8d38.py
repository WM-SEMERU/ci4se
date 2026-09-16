def get_history_by_tail_number(self, tail_number, page=1, limit=100):
    url = REG_BASE.format(tail_number, str(self.AUTH_TOKEN), page, limit)
    return self._fr24.get_data(url, True)