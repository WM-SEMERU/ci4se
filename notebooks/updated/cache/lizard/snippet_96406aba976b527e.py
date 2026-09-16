def set_board_options(self, options, team_context, id):
    project = None
    team = None
    if team_context is not None:
        if team_context.project_id:
            project = team_context.project_id
        else:
            project = team_context.project
        if team_context.team_id:
            team = team_context.team_id
        else:
            team = team_context.team
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project,
            'string')
    if team is not None:
        route_values['team'] = self._serialize.url('team', team, 'string')
    if id is not None:
        route_values['id'] = self._serialize.url('id', id, 'str')
    content = self._serialize.body(options, '{str}')
    response = self._send(http_method='PUT', location_id=
        '23ad19fc-3b8e-4877-8462-b3f92bc06b40', version='5.0', route_values
        =route_values, content=content)
    return self._deserialize('{str}', self._unwrap_collection(response))