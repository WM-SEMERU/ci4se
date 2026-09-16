def to_query(self):
    return {self.name: {'lang': self.lang, 'script': self.script, 'params':
        self.script_params}}