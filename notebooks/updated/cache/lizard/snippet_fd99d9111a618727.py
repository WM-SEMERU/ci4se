def _get_result_paths(self, output_dir):
    self._write_properties_file()
    properties_fp = os.path.join(self.ModelDir, self.PropertiesFile)
    result_paths = {'properties': ResultPath(properties_fp, IsWritten=True)}
    return result_paths