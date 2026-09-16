def create_package_file(root, master_package, subroot, py_files, opts, subs):
    package = os.path.split(root)[-1]
    text = format_heading(1, '%s Package' % package)
    for py_file in py_files:
        if shall_skip(os.path.join(root, py_file)):
            continue
        is_package = py_file == INIT
        py_file = os.path.splitext(py_file)[0]
        py_path = makename(subroot, py_file)
        if is_package:
            heading = ':mod:`%s` Package' % package
        else:
            heading = ':mod:`%s` Module' % py_file
        text += format_heading(2, heading)
        text += format_directive(is_package and subroot or py_path,
            master_package)
        text += '\n'
    subs = [sub for sub in subs if os.path.isfile(os.path.join(root, sub,
        INIT))]
    if subs:
        text += format_heading(2, 'Subpackages')
        text += '.. toctree::\n\n'
        for sub in subs:
            text += '    %s.%s\n' % (makename(master_package, subroot), sub)
        text += '\n'
    write_file(makename(master_package, subroot), text, opts)