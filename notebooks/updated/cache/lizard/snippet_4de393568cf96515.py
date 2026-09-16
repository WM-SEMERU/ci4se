def visit_any_conditionnal(self, node1, node2):
    true_naming = false_naming = None
    try:
        tmp = self.naming.copy()
        for expr in node1:
            self.visit(expr)
        true_naming = self.naming
        self.naming = tmp
    except KeyError:
        pass
    try:
        tmp = self.naming.copy()
        for expr in node2:
            self.visit(expr)
        false_naming = self.naming
        self.naming = tmp
    except KeyError:
        pass
    if true_naming and not false_naming:
        self.naming = true_naming
    elif false_naming and not true_naming:
        self.naming = false_naming
    elif true_naming and false_naming:
        self.naming = false_naming
        for k, v in true_naming.items():
            if k not in self.naming:
                self.naming[k] = v
            else:
                for dep in v:
                    if dep not in self.naming[k]:
                        self.naming[k].append(dep)