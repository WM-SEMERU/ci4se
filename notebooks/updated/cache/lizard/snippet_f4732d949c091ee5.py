def query_paths(self):
    output = self.namespace.alias_to_query_paths.get(self.name)
    if output:
        return output
    Log.error('Can not find index {{index|quote}}', index=self.name)