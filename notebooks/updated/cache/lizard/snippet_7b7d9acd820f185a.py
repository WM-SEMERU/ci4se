def date(self, col: str, **kwargs):
    try:
        self.df[col] = pd.to_datetime(self.df[col], **kwargs)
    except Exception as e:
        self.err(e, 'Can not convert to date')