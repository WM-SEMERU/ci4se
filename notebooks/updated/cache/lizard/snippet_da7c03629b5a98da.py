def convert_and_execute_notebook(self, name):
    self.convert_notebook(name)
    code = self.read_code(name)
    exec(code, globals())