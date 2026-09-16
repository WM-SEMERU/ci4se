def _FileFetchFailed(self, index, request_name):
    pathspec, request_data = self._RemoveCompletedPathspec(index)
    self.FileFetchFailed(pathspec, request_name, request_data=request_data)