def __parse_json_file(self, file_path):
    if file_path == '' or os.path.splitext(file_path)[1] != '.json':
        raise IOError('Invalid Json file')
    with open(file_path) as json_file:
        self._raw_data = json.load(json_file)
    self._json_data = copy.deepcopy(self._raw_data)