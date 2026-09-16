def compileUiDir(dir, recurse=False, map=None, **compileUi_args):
    import os

    def compile_ui(ui_dir, ui_file):
        if ui_file.endswith('.ui'):
            py_dir = ui_dir
            py_file = ui_file[:-3] + '.py'
            if map is not None:
                py_dir, py_file = map(py_dir, py_file)
            try:
                os.makedirs(py_dir)
            except:
                pass
            ui_path = os.path.join(ui_dir, ui_file)
            py_path = os.path.join(py_dir, py_file)
            ui_file = open(ui_path, 'r')
            py_file = open(py_path, 'w')
            try:
                compileUi(ui_file, py_file, **compileUi_args)
            finally:
                ui_file.close()
                py_file.close()
    if recurse:
        for root, _, files in os.walk(dir):
            for ui in files:
                compile_ui(root, ui)
    else:
        for ui in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, ui)):
                compile_ui(dir, ui)