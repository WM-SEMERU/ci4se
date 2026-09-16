def _evaluate(self, message):
    return eval(self.code, globals(), {'J': message, 'timedelta': timedelta,
        'datetime': datetime, 'SKIP': self._SKIP})