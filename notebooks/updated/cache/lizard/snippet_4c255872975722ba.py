def add_child(self, child):
    if child:
        if child.tag in self.contained_children:
            self.children.append(child)
        else:
            raise ETD_MS_StructureException(
                'Invalid child "%s" for parent "%s"' % (child.tag, self.tag))