def extract_translations(self, string):
    tree = ast.parse(string)
    visitor = TransVisitor(self.tranz_functions, self.tranzchoice_functions)
    visitor.visit(tree)
    return visitor.translations