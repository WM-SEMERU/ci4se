def load_file(self, input_file):
    pyimg = imp.load_source('image2py_taf', input_file)
    self.files = pyimg.data
    self.set_template(templates.templateByName(pyimg.template))