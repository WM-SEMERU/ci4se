def _read_dataset_metadata(self):
    blob = self.storage_client.get_blob('dataset/' + self.dataset_name +
        '_dataset.csv')
    buf = BytesIO()
    blob.download_to_file(buf)
    buf.seek(0)
    return eval_lib.DatasetMetadata(buf)