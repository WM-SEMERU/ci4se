def settlement_date(self, value):
    if value:
        self._settlement_date = parse(value).date() if isinstance(value,
            type_check) else value