def convert_to_sqlite(self, destination=None, method='shell', progress=False):
    if progress:
        progress = tqdm.tqdm
    else:
        progress = lambda x: x
    if destination is None:
        destination = self.replace_extension('sqlite')
    destination.remove()
    if method == 'shell':
        return self.sqlite_by_shell(destination)
    if method == 'object':
        return self.sqlite_by_object(destination, progress)
    if method == 'dataframe':
        return self.sqlite_by_df(destination, progress)