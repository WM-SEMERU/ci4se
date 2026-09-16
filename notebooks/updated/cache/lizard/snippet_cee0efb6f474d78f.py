def RunMetadata(self, tag):
    if tag not in self._tagged_metadata:
        raise ValueError('There is no run metadata with this tag name')
    run_metadata = config_pb2.RunMetadata()
    run_metadata.ParseFromString(self._tagged_metadata[tag])
    return run_metadata