def to_output(self, value):
    return json.loads(resolwe_runtime_utils.save_file(self.name, value.path,
        *value.refs))