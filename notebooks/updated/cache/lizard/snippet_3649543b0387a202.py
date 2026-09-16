def load_from_file(filepath):
    class_inst = None
    expected_class = 'Py3status'
    module_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])
    if file_ext.lower() == '.py':
        py_mod = imp.load_source(module_name, filepath)
        if hasattr(py_mod, expected_class):
            class_inst = py_mod.Py3status()
    return class_inst