def yaml_from_file(self, fpath):
    lookup = self._load_param_file(fpath)
    if not lookup:
        return
    content = '\n'.join(self.content)
    parsed = yaml.safe_load(content)
    new_content = list()
    for paramlist in parsed:
        if not isinstance(paramlist, dict):
            self.app.warn(
                'Invalid parameter definition ``%s``. Expected format: ``name: reference``.  Skipping.'
                 % paramlist, (self.state_machine.node.source, self.
                state_machine.node.line))
            continue
        for name, ref in paramlist.items():
            if ref in lookup:
                new_content.append((name, lookup[ref]))
            else:
                self.app.warn(
                    'No field definition for ``%s`` found in ``%s``.  Skipping.'
                     % (ref, fpath), (self.state_machine.node.source, self.
                    state_machine.node.line))
    self.yaml = new_content