def _read_routine_metadata(self):
    metadata = {}
    if os.path.isfile(self._metadata_filename):
        with open(self._metadata_filename, 'r') as file:
            metadata = json.load(file)
    return metadata