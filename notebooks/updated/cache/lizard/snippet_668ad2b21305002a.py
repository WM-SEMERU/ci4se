def save_dataset(self, dataset_id, filename=None, writer=None, overlay=None,
    compute=True, **kwargs):
    if writer is None and filename is None:
        writer = 'geotiff'
    elif writer is None:
        writer = self.get_writer_by_ext(os.path.splitext(filename)[1])
    writer, save_kwargs = load_writer(writer, ppp_config_dir=self.
        ppp_config_dir, filename=filename, **kwargs)
    return writer.save_dataset(self[dataset_id], overlay=overlay, compute=
        compute, **save_kwargs)