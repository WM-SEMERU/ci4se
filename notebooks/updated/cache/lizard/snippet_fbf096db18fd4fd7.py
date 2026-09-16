def _get_container(self, path):
    bucket = self.native_conn.get_bucket(path)
    return self.cont_cls.from_bucket(self, bucket)