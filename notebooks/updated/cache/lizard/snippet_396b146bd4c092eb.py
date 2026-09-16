def get_stack_info(frames):
    __traceback_hide__ = True
    results = []
    for frame_info in frames:
        if isinstance(frame_info, (list, tuple)):
            frame, lineno = frame_info
        else:
            frame = frame_info
            lineno = frame_info.f_lineno
        f_locals = getattr(frame, 'f_locals', {})
        if _getitem_from_frame(f_locals, '__traceback_hide__'):
            continue
        f_globals = getattr(frame, 'f_globals', {})
        loader = _getitem_from_frame(f_globals, '__loader__')
        module_name = _getitem_from_frame(f_globals, '__name__')
        f_code = getattr(frame, 'f_code', None)
        if f_code:
            abs_path = frame.f_code.co_filename
            function = frame.f_code.co_name
        else:
            abs_path = None
            function = None
        if lineno:
            lineno -= 1
        if lineno is not None and abs_path:
            context = get_lines_from_file(abs_path, lineno, 3, loader,
                module_name)
        else:
            context = []
        try:
            base_filename = sys.modules[module_name.split('.', 1)[0]].__file__
            filename = abs_path.split(base_filename.rsplit('/', 2)[0], 1)[-1][
                1:]
        except:
            filename = abs_path
        if not filename:
            filename = abs_path
        frame_result = {'abs_path': abs_path, 'filename': filename,
            'module': module_name, 'function': function, 'lineno': lineno +
            1, 'context': context}
        results.append(frame_result)
    return results