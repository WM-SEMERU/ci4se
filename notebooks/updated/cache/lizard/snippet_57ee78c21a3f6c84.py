def firstPass(ASTs, verbose):
    fdefs = dict()
    cdefs = dict()
    imp_obj_strs = dict()
    imp_mods = dict()
    for root, path in ASTs:
        fdefs[path] = []
        fdefs[path].append(formatBodyNode(root, path))
        imp_obj_strs[path] = []
        imp_mods[path] = []
        cdefs[path] = []
        for node, stack in traversal(root):
            if isinstance(node, ast.FunctionDef):
                fdefs[path].append(formatFunctionNode(node, path, stack))
            elif isinstance(node, ast.ImportFrom):
                module = ia.getImportFromModule(node, path, verbose)
                if module:
                    fn_names = ia.getImportFromObjects(node)
                    for fn_name in fn_names:
                        imp_obj_strs[path].append((module, fn_name))
                elif verbose:
                    print('No module found ' + ast.dump(node))
            elif isinstance(node, ast.Import):
                module = ia.getImportModule(node, path, verbose)
                imp_mods[path].append(module)
            elif isinstance(node, ast.ClassDef):
                node.path = path
                cdefs[path].append(node)
    return fdefs, imp_obj_strs, imp_mods, cdefs