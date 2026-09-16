def download(self, version=None, tags=None, ext=None, overwrite=False,
    verbose=False, **kwargs):
    fpath = self.fpath(version=version, tags=tags, ext=ext)
    if os.path.isfile(fpath) and not overwrite:
        if verbose:
            print(
                'File exists and overwrite set to False, so not downloading {} with version={} and tags={}'
                .format(self.name, version, tags))
            return
    download_dataset(dataset_name=self.name, file_path=fpath, task=self.
        task, dataset_attributes=self.kwargs, **kwargs)