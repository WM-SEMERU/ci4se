def internal_change_variable_json(py_db, request):
    arguments = request.arguments
    variables_reference = arguments.variablesReference
    fmt = arguments.format
    if hasattr(fmt, 'to_dict'):
        fmt = fmt.to_dict()
    frame_variable = py_db.suspended_frames_manager.get_variable(
        variables_reference)
    if hasattr(frame_variable, 'frame'):
        frame = frame_variable.frame
        pydevd_vars.change_attr_expression(frame, arguments.name, arguments
            .value, py_db)
        for child_var in frame_variable.get_children_variables(fmt=fmt):
            if child_var.get_name() == arguments.name:
                var_data = child_var.get_var_data(fmt=fmt)
                body = SetVariableResponseBody(value=var_data['value'],
                    type=var_data['type'], variablesReference=var_data.get(
                    'variablesReference'), namedVariables=var_data.get(
                    'namedVariables'), indexedVariables=var_data.get(
                    'indexedVariables'))
                variables_response = pydevd_base_schema.build_response(request,
                    kwargs={'body': body})
                py_db.writer.add_command(NetCommand(CMD_RETURN, 0,
                    variables_response, is_json=True))
                break
    body = SetVariableResponseBody('')
    variables_response = pydevd_base_schema.build_response(request, kwargs=
        {'body': body, 'success': False, 'message': 'Unable to change: %s.' %
        (arguments.name,)})
    return NetCommand(CMD_RETURN, 0, variables_response, is_json=True)