def validate():
    assert isinstance(request.json, dict), 'invalid payload format.'
    data = request.json
    assert isinstance(data, dict
        ), 'invalid `body` type, should be formatted as a dict.'
    if is_valid_dict(data):
        return jsonify(True)
    else:
        error_list = list()
        for err in list_errors_dict_local(data):
            stack_path = list(err[1].relative_path)
            stack_path = [str(p) for p in stack_path]
            this_err_response = {'path': '/'.join(stack_path), 'message':
                err[1].message}
            error_list.append(this_err_response)
        res = jsonify(error_list)
        return res