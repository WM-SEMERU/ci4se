def get_uri_schemaloc_map(self):
    mapping = {}
    for ni in six.itervalues(self.__ns_uri_map):
        if ni.schema_location:
            mapping[ni.uri] = ni.schema_location
    return mapping