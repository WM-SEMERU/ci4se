def get_configuration_dict(self, secret_attrs=False):
    cd = {'repo_nexml2json': self.repo_nexml2json, 'number_of_shards': len(
        self._shards), 'initialization': self._filepath_args, 'shards': []}
    for i in self._shards:
        cd['shards'].append(i.get_configuration_dict(secret_attrs=secret_attrs)
            )
    return cd