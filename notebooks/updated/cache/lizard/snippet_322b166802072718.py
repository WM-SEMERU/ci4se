def _fetch_events_files_on_disk(self):
    all_files = tf.io.gfile.listdir(self._events_directory)
    relevant_files = [file_name for file_name in all_files if
        _DEBUGGER_EVENTS_FILE_NAME_REGEX.match(file_name)]
    return sorted(relevant_files, key=self._obtain_file_index)