def oedit(obj, modal=True, namespace=None):
    from spyder.utils.qthelpers import qapplication
    app = qapplication()
    if modal:
        obj_name = ''
    else:
        assert is_text_string(obj)
        obj_name = obj
        if namespace is None:
            namespace = globals()
        keeper.set_namespace(namespace)
        obj = namespace[obj_name]
        namespace['__qapp__'] = app
    result = create_dialog(obj, obj_name)
    if result is None:
        return
    dialog, end_func = result
    if modal:
        if dialog.exec_():
            return end_func(dialog)
    else:
        keeper.create_dialog(dialog, obj_name, end_func)
        import os
        if os.name == 'nt':
            app.exec_()