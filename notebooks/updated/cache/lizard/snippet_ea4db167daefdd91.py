def __flush(self):
    try:
        self.__flush_buffer()
        self._file['md5'] = self._file['md5'].hexdigest()
        self._file['length'] = self._position
        self._file['uploadDate'] = datetime.datetime.utcnow()
        return self._coll.files.insert_one(self._file)
    except DuplicateKeyError:
        self._raise_file_exists(self._id)