def find_copies(input_dir, exclude_list):
    copies = []

    def copy_finder(copies, dirname):
        for obj in os.listdir(dirname):
            pathname = os.path.join(dirname, obj)
            if os.path.isdir(pathname):
                continue
            if obj in exclude_list:
                continue
            if obj.endswith('.mustache'):
                continue
            copies.append(os.path.join(dirname, obj))
    dir_visitor(input_dir, functools.partial(copy_finder, copies))
    return copies