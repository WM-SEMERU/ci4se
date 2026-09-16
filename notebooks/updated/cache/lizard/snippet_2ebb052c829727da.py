def on_assert(self, node):
    if not self.run(node.test):
        self.raise_exception(node, exc=AssertionError, msg=node.msg)
    return True