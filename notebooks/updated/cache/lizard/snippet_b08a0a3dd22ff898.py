def create_args(args, root):
    extension_args = {}
    for arg in args:
        parse_extension_arg(arg, extension_args)
    for name in sorted(extension_args, key=len):
        path = name.split('.')
        update_namespace(root, path, extension_args[name])