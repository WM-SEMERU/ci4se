def remove_breakpoint(self, py_db, filename, breakpoint_type, breakpoint_id):
    file_to_id_to_breakpoint = None
    if breakpoint_type == 'python-line':
        breakpoints = py_db.breakpoints
        file_to_id_to_breakpoint = py_db.file_to_id_to_line_breakpoint
    elif py_db.plugin is not None:
        result = py_db.plugin.get_breakpoints(py_db, breakpoint_type)
        if result is not None:
            file_to_id_to_breakpoint = py_db.file_to_id_to_plugin_breakpoint
            breakpoints = result
    if file_to_id_to_breakpoint is None:
        pydev_log.critical(
            'Error removing breakpoint. Cannot handle breakpoint of type %s',
            breakpoint_type)
    else:
        try:
            id_to_pybreakpoint = file_to_id_to_breakpoint.get(filename, {})
            if DebugInfoHolder.DEBUG_TRACE_BREAKPOINTS > 0:
                existing = id_to_pybreakpoint[breakpoint_id]
                pydev_log.info(
                    'Removed breakpoint:%s - line:%s - func_name:%s (id: %s)\n'
                     % (filename, existing.line, existing.func_name.encode(
                    'utf-8'), breakpoint_id))
            del id_to_pybreakpoint[breakpoint_id]
            py_db.consolidate_breakpoints(filename, id_to_pybreakpoint,
                breakpoints)
            if py_db.plugin is not None:
                py_db.has_plugin_line_breaks = py_db.plugin.has_line_breaks()
        except KeyError:
            pydev_log.info(
                """Error removing breakpoint: Breakpoint id not found: %s id: %s. Available ids: %s
"""
                , filename, breakpoint_id, dict_keys(id_to_pybreakpoint))
    py_db.on_breakpoints_changed(removed=True)