def _UploadChunk(self, chunk):
    blob = _CompressedDataBlob(chunk)
    self._action.ChargeBytesToSession(len(chunk.data))
    self._action.SendReply(blob, session_id=self._TRANSFER_STORE_SESSION_ID)
    return rdf_client_fs.BlobImageChunkDescriptor(digest=hashlib.sha256(
        chunk.data).digest(), offset=chunk.offset, length=len(chunk.data))