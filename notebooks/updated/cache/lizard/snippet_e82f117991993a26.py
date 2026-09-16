def _get_md5sum(self, fpath):
    try:
        current_md5 = hashlib.md5()
        if isinstance(fpath, six.string_types) and os.path.exists(fpath):
            with open(fpath, 'rb') as fh:
                for chunk in self._read_chunks(fh):
                    current_md5.update(chunk)
        elif fpath.__class__.__name__ in ['StringIO', 'StringO'] or isinstance(
            fpath, IOBase):
            for chunk in self._read_chunks(fpath):
                current_md5.update(chunk)
        else:
            return ''
        return current_md5.hexdigest()
    except Exception:
        msg = "Failed to calculate the image's md5sum"
        LOG.error(msg)
        raise exception.SDKImageOperationError(rs=3)