def add(self, name, obj=None):
    if obj:
        text = '\n::\n\n' + indent(str(obj))
    else:
        text = views.view(name, self.dstore)
    if text:
        title = self.title[name]
        line = '-' * len(title)
        self.text += '\n'.join(['\n\n' + title, line, text])