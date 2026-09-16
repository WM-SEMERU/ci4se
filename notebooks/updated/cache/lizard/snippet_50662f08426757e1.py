def merge(self, groupBy=None):
    if isinstance(groupBy, list) and all([isinstance(x, str) for x in groupBy]
        ):
        groupBy = Some(groupBy)
    elif groupBy is None:
        groupBy = none()
    else:
        raise TypeError('groupBy must be a list of strings. {} was provided'
            .format(type(groupBy)))
    new_index = self.opmng.merge(self.__index, groupBy)
    return GMQLDataset(index=new_index, location=self.location,
        local_sources=self._local_sources, remote_sources=self.
        _remote_sources, meta_profile=self.meta_profile)