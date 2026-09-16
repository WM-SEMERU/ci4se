def digest(self, **args):
    return String(XML.canonicalized_string(self.root)).digest(**args)