def connect(self):
    self.conn = boto.connect_s3(self.AWS_ACCESS_KEY_ID, self.
        AWS_SECRET_ACCESS_KEY, debug=self.S3UTILS_DEBUG_LEVEL)
    self.bucket = self.conn.get_bucket(self.AWS_STORAGE_BUCKET_NAME)
    self.k = Key(self.bucket)