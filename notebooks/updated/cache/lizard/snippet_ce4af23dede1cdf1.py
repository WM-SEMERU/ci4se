def get(self, file_path, ref, **kwargs):
    file_path = file_path.replace('/', '%2F')
    return GetMixin.get(self, file_path, ref=ref, **kwargs)