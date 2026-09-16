def _uploadStream(self, fileName, update=False, encrypt=True):
    blob = self.bucket.blob(bytes(fileName), encryption_key=self.sseKey if
        encrypt else None)


    class UploadPipe(WritablePipe):

        def readFrom(self, readable):
            if not update:
                assert not blob.exists()
            blob.upload_from_file(readable)
    with UploadPipe() as writable:
        yield writable