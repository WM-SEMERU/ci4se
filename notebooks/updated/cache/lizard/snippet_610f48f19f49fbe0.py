def input(self, what):
    if what is None:
        return None
    if not isinstance(what, STRING_TYPES):
        return self._input_json_from_non_string(what)
    if path.isfile(what):
        return self._input_json_from_file(what)
    try:
        return self._input_json_as_string(what)
    except ValueError:
        return self._input_string(what)