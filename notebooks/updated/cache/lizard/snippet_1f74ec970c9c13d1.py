def get_metadata(self):
    if self.path_or_name is None:
        raise ValueError(
            'You cannot explore the metadata of an intermediate query.You can get metadata only after a load_from_local or load_from_remote'
            )
    if self.location == 'local':
        return self.__get_metadata_local()
    elif self.location == 'remote':
        return self.__get_metadata_remote()