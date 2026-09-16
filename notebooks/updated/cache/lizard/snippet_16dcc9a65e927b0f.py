def insert(self, i, x):
    if i == len(self):
        self.append(x)
    elif len(self.matches) > i:
        insert_index = self.matches[i].getparent().index(self.matches[i])
        _create_xml_node(self.xast, self.node, self.context, insert_index)
        self[i] = x
    else:
        raise IndexError(
            "Can't insert '%s' at index %d - list length is only %d" % (x,
            i, len(self)))