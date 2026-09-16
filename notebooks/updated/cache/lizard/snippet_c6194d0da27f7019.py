def relative_path(sub_directory='', function_index=1):
    frm = inspect.currentframe()
    for i in range(function_index):
        frm = frm.f_back
    if frm.f_code.co_name == 'run_code':
        frm = frm.f_back
    if not isinstance(sub_directory, list):
        sub_directory = sub_directory.replace('\\', '/').split('/')
    path = os.path.split(frm.f_code.co_filename)[0]
    if sub_directory:
        path = os.path.abspath(os.path.join(path, *sub_directory))
    return path