def GetNumberOfRows(self):
    file_object = self.GetFileObject()
    if not file_object:
        raise errors.BackEndError(
            'Unable to retrieve SQLite blob file-like object.')
    try:
        self._number_of_entries = file_object.GetNumberOfRows()
    finally:
        file_object.close()
    return self._number_of_entries