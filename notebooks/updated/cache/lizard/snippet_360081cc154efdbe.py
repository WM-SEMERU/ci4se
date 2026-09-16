def print_declarations(decls, detailed=True, recursive=True, writer=lambda
    x: sys.stdout.write(x + os.linesep), verbose=True):
    prn = decl_printer_t(0, detailed, recursive, writer, verbose=verbose)
    if not isinstance(decls, list):
        decls = [decls]
    for d in decls:
        prn.level = 0
        prn.instance = d
        algorithm.apply_visitor(prn, d)