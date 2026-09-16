def dc_element(self, parent, name, text):
    if self.dc_uri in self.namespaces:
        dcel = SchemaNode(self.namespaces[self.dc_uri] + ':' + name, text=text)
        parent.children.insert(0, dcel)