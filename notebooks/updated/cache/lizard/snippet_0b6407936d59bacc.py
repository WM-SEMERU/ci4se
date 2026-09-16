def find_c_file(obj_file, vpath):
    c_file = None
    relative_c_file = os.path.splitext(obj_file)[0] + '.c'
    relative_c_file = relative_c_file.lstrip('/\\')
    for p in vpath:
        possible_c_file = os.path.join(p, relative_c_file)
        if os.path.exists(possible_c_file):
            c_file = possible_c_file
            break
    return c_file