def ReadBlobs(self, blob_ids):
    result = {}
    for blob_id in blob_ids:
        result[blob_id] = self.blobs.get(blob_id, None)
    return result