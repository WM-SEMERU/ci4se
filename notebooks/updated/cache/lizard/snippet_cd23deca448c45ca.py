def _readContents(self, jobStoreID):
    job = self.bucket.get_blob(bytes(jobStoreID), encryption_key=self.sseKey)
    if job is None:
        raise NoSuchJobException(jobStoreID)
    return job.download_as_string()