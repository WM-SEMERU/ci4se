def _importFile(self, otherCls, url, sharedFileName=None, hardlink=False):
    if sharedFileName is None:
        with self.writeFileStream() as (writable, jobStoreFileID):
            otherCls._readFromUrl(url, writable)
            return FileID(jobStoreFileID, otherCls.getSize(url))
    else:
        self._requireValidSharedFileName(sharedFileName)
        with self.writeSharedFileStream(sharedFileName) as writable:
            otherCls._readFromUrl(url, writable)
            return None