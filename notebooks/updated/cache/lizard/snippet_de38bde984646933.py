def tell_async(self, data, timeout=10, mime=None):
    logger.info('tell(timeout=%s) [subid=%s]', timeout, self.subid)
    if mime is None and isinstance(data, PointDataObject):
        data = data.to_dict()
    return self._client._request_sub_tell(self.subid, data, timeout, mime=mime)