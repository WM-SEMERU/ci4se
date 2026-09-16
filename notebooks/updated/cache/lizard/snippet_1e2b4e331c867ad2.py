def save_datasets(self, writer='geotiff', datasets=None, compute=True, **kwargs
    ):
    if datasets is not None:
        datasets = [self[ds] for ds in datasets]
    else:
        datasets = [self.datasets.get(ds) for ds in self.wishlist]
        datasets = [ds for ds in datasets if ds is not None]
    if not datasets:
        raise RuntimeError(
            'None of the requested datasets have been generated or could not be loaded. Requested composite inputs may need to have matching dimensions (eg. through resampling).'
            )
    writer, save_kwargs = load_writer(writer, ppp_config_dir=self.
        ppp_config_dir, **kwargs)
    return writer.save_datasets(datasets, compute=compute, **save_kwargs)