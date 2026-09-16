def write_dataframe(self, result, dst_paths, nodata=None, compress='lzw'):
    result = self._convert_to_ndarray(result)
    self.write_ndarray(result, dst_paths, nodata=nodata, compress=compress)