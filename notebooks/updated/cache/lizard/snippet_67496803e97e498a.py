def __find_source_files(self):
    for dir_path, _, files in os.walk(self._source_directory):
        for name in files:
            if name.lower().endswith(self._source_file_extension):
                basename = os.path.splitext(os.path.basename(name))[0]
                relative_path = os.path.relpath(os.path.join(dir_path, name))
                if basename in self._source_file_names:
                    self._io.error(
                        "Files '{0}' and '{1}' have the same basename.".
                        format(self._source_file_names[basename],
                        relative_path))
                    self.error_file_names.add(relative_path)
                else:
                    self._source_file_names[basename] = relative_path