def visit_Placeholder(self, pattern):
    if pattern.id in self.placeholders and not Check(self.node, self.
        placeholders).visit(self.placeholders[pattern.id]):
        return False
    else:
        self.placeholders[pattern.id] = self.node
        return True