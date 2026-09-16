def AppendContent(self, src_fd):
    while 1:
        blob = src_fd.read(self.chunksize)
        if not blob:
            break
        blob_id = data_store.BLOBS.WriteBlobWithUnknownHash(blob)
        self.AddBlob(blob_id, len(blob))
    self.Flush()