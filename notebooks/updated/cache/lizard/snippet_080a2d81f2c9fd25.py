def get(self, s3_path, destination_local_path):
    bucket, key = self._path_to_bucket_and_key(s3_path)
    self.s3.meta.client.download_file(bucket, key, destination_local_path)