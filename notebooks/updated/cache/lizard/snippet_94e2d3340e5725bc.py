def rollforward(self):
    if self.contents['rollforward'] is None:
        raise ValueError('No operation to roll forward on refpkg')
    new_log_message = self.contents['rollforward'][0]
    new_contents = self.contents['rollforward'][1]
    new_contents['log'] = [new_log_message] + self.contents.pop('log')
    self.contents['rollforward'] = None
    new_contents['rollback'] = copy.deepcopy(self.contents)
    new_contents['rollback'].pop('rollforward')
    self.contents = new_contents
    self._sync_to_disk()