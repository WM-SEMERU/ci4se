def to_dataframe(self, read_session, dtypes=None):
    if fastavro is None:
        raise ImportError(_FASTAVRO_REQUIRED)
    if pandas is None:
        raise ImportError(_PANDAS_REQUIRED)
    return self.rows(read_session).to_dataframe(dtypes=dtypes)