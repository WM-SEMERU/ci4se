def _screen(self, include=True, **kwargs):
    df = self.copy()
    for k, v in list(kwargs.items()):
        v = [v] if type(v) != list else v
        if include:
            df = df[df[k].str.contains('|'.join(v), flags=re.IGNORECASE).
                fillna(False)]
        else:
            df = df[df[k].str.contains('|'.join(v), flags=re.IGNORECASE).
                fillna(False) == False]
    return df