def to_int(self, *cols, **kwargs):
    try:
        for col in cols:
            self.df[col] = pd.to_numeric(self.df[col], **kwargs)
    except Exception as e:
        self.err(e, 'Can not convert column values to integer')
        return
    self.ok('Converted column values to integers')