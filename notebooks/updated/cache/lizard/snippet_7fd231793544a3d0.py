def decode(self, json_string):
    default_obj = super(JSONPDecoder, self).decode(json_string)
    return list(self._iterdecode(default_obj))[0]