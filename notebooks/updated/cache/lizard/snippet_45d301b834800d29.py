def process_omp_attachements(self, node, stmt, index=None):
    omp_directives = metadata.get(node, OMPDirective)
    if omp_directives:
        directives = list()
        for directive in omp_directives:
            directive.deps = [self.visit(dep) for dep in directive.deps]
            directives.append(directive)
        if index is None:
            stmt = AnnotatedStatement(stmt, directives)
        else:
            stmt[index] = AnnotatedStatement(stmt[index], directives)
    return stmt