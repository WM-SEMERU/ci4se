def trimsquants(self, col: str, sup: float):
    try:
        self.df = self._trimquants(col, None, sup)
    except Exception as e:
        self.err(e, self.trimsquants, 'Can not trim superior quantiles')