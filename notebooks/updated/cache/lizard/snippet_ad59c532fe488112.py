def add_code_cell(self, content, tags=None):
    self.notebook['cells'].append(nb.v4.new_code_cell(content, **{
        'metadata': {'tags': tags}}))