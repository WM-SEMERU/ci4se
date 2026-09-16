def files(self):
    if self.model is None:
        raise MissingModelError()
    records_buckets = RecordsBuckets.query.filter_by(record_id=self.id).first()
    if not records_buckets:
        bucket = self._create_bucket()
        if not bucket:
            return None
        RecordsBuckets.create(record=self.model, bucket=bucket)
    else:
        bucket = records_buckets.bucket
    return self.files_iter_cls(self, bucket=bucket, file_cls=self.file_cls)