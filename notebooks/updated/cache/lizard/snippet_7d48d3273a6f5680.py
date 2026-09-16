def seek(self, offset, whence=SEEK_SET):
    if whence == SEEK_SET:
        self.__sf.seek(offset)
    elif whence == SEEK_CUR:
        self.__sf.seek(self.tell() + offset)
    elif whence == SEEK_END:
        self.__sf.seek(self.__sf.filesize - offset)