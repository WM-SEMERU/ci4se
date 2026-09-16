def inline_inputs(self):
    self.text = texutils.inline(self.text, os.path.dirname(self._filepath))
    self._children = {}