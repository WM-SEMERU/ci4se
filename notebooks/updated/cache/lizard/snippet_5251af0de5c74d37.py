def enable_global_annotations_decorator(flag=True, retrospective=True):
    global global_annotations_decorator
    global_annotations_decorator = flag
    if import_hook_enabled:
        _install_import_hook()
    if global_annotations_decorator and retrospective:
        _catch_up_global_annotations_decorator()
    return global_annotations_decorator