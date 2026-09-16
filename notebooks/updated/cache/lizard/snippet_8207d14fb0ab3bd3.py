def get(self, bucket=None, versions=missing, uploads=missing):
    if uploads is not missing:
        return self.multipart_listuploads(bucket)
    else:
        return self.listobjects(bucket, versions)