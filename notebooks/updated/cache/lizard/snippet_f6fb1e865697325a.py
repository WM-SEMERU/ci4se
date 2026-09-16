def compile(self, ast):
    documents = {}
    imports = util.StringBuilder()
    for imp in ast.imports:
        if imp.static or imp.wildcard:
            continue
        package_parts = []
        cls_parts = []
        for part in imp.path.split('.'):
            if cls_parts or part[0].isupper():
                cls_parts.append(part)
            else:
                package_parts.append(part)
        if cls_parts == []:
            cls_parts.append(package_parts.pop())
        package = '.'.join(package_parts)
        cls = '.'.join(cls_parts)
        imports.append(util.Directive('java:import', package + ' ' + cls).
            build())
    import_block = imports.build()
    if not ast.package:
        raise ValueError('File must have package declaration')
    package = ast.package.name
    type_declarations = []
    for path, node in ast.filter(javalang.tree.TypeDeclaration):
        if not self.filter(node):
            continue
        classes = [n.name for n in path if isinstance(n, javalang.tree.
            TypeDeclaration)]
        classes.append(node.name)
        name = '.'.join(classes)
        type_declarations.append((package, name, node))
    for package, name, declaration in type_declarations:
        full_name = package + '.' + name
        document = self.compile_type_document(import_block, package, name,
            declaration)
        documents[full_name] = package, name, document.build()
    return documents