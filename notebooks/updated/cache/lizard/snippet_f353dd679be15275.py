def visit_annassign(self, node):
    target = node.target.accept(self)
    annotation = node.annotation.accept(self)
    if node.value is None:
        return '%s: %s' % (target, annotation)
    return '%s: %s = %s' % (target, annotation, node.value.accept(self))