def seek(self, pos, whence=os.SEEK_SET):
    if whence == os.SEEK_SET:
        new_pos = pos
    elif whence == os.SEEK_CUR:
        new_pos = self.__position + pos
    elif whence == os.SEEK_END:
        new_pos = int(self.length) + pos
    else:
        raise IOError(22, 'TxMongo: invalid value for `whence`')
    if new_pos < 0:
        raise IOError(22, 'TxMongo: invalid value for `pos` - must be positive'
            )
    self.__position = new_pos