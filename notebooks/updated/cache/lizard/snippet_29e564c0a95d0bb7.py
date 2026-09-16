def _set_splits(self, split_dict):
    self._splits = split_dict.copy()
    del self.as_proto.splits[:]
    for split_info in split_dict.to_proto():
        self.as_proto.splits.add().CopyFrom(split_info)