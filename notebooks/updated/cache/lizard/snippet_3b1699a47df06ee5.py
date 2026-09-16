def sessions(self):
    return pd.to_datetime(reduce(np.union1d, (reader.dates for reader in
        self._readers.values())), utc=True)