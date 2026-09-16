def _cube_dict(self):
    try:
        cube_response = self._cube_response_arg
        cube_dict = cube_response if isinstance(cube_response, dict
            ) else json.loads(cube_response)
        return cube_dict.get('value', cube_dict)
    except TypeError:
        raise TypeError(
            'Unsupported type <%s> provided. Cube response must be JSON (str) or dict.'
             % type(self._cube_response_arg).__name__)