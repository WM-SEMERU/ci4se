def visit_Module(self, node):
    deps = sorted(self.dependencies)
    headers = [Include(os.path.join('pythonic', 'include', *t) + '.hpp') for
        t in deps]
    headers += [Include(os.path.join('pythonic', *t) + '.hpp') for t in deps]
    decls_n_defns = [self.visit(stmt) for stmt in node.body]
    decls, defns = zip(*[s for s in decls_n_defns if s])
    nsbody = [s for ls in decls + defns for s in ls]
    ns = Namespace(pythran_ward + self.passmanager.module_name, nsbody)
    self.result = CompilationUnit(headers + [ns])