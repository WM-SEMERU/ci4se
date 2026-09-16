def visit_index(self, node, parent):
    newnode = nodes.Index(parent=parent)
    newnode.postinit(self.visit(node.value, newnode))
    return newnode