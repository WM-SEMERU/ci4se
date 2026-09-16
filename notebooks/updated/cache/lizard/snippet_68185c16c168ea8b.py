def update_file(self, filepath, df, notes=None):
    assert isinstance(df, pd.DataFrame
        ), "Cannot update file with type '{}'".format(type(df))
    self._models[filepath].setDataFrame(df, copyDataFrame=False)
    if notes:
        update = dict(date=pd.Timestamp(datetime.datetime.now()), notes=notes)
        self._updates[filepath].append(update)
    self._paths_updated.append(filepath)