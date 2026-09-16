def new_action(project_id):
    project = get_data_or_404('project', project_id)
    if project['owner_id'] != get_current_user_id():
        return jsonify(message='forbidden'), 403
    form = NewActionForm()
    if not form.validate_on_submit():
        return jsonify(errors=form.errors), 400
    data = form.data
    data['project_id'] = project_id
    id = add_instance('action', **data)
    if not id:
        return jsonify(errors={'name': ['duplicated slug.']}), 400
    action = get_data_or_404('action', id)
    return jsonify(**action)