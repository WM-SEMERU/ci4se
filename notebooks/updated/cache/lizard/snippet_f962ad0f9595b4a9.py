def fdate(self, *cols, precision: str='S', format: str=None):

    def formatdate(row):
        return row.strftime(format)

    def convert(row):
        encoded = '%Y-%m-%d %H:%M:%S'
        if precision == 'Min':
            encoded = '%Y-%m-%d %H:%M'
        elif precision == 'H':
            encoded = '%Y-%m-%d %H'
        elif precision == 'D':
            encoded = '%Y-%m-%d'
        elif precision == 'M':
            encoded = '%Y-%m'
        elif precision == 'Y':
            encoded = '%Y'
        return row.strftime(encoded)
    try:
        for f in cols:
            try:
                if format is None:
                    self.df[f] = pd.to_datetime(self.df[f]).apply(convert)
                else:
                    self.df[f] = pd.to_datetime(self.df[f]).apply(formatdate)
            except ValueError as e:
                self.err(e, 'Can not convert date')
                return
    except KeyError:
        self.warning('Can not find colums ' + ' '.join(cols))
        return
    except Exception as e:
        self.err(e, 'Can not process date col')