def load_commands(self, parser):
    entrypoints = self._get_entrypoints()
    already_loaded = set()
    for entrypoint in entrypoints:
        if entrypoint.name not in already_loaded:
            command_class = entrypoint.load()
            command_class(entrypoint.name, self, parser).prepare()
            already_loaded.add(entrypoint.name)