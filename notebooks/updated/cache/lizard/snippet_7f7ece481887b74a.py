def to_literal(self):
    if not self.nodes:
        return self.tag, self.attrib, self.text, []
    else:
        return self.tag, self.attrib, self.text, list(map(to_literal, self.
            nodes))