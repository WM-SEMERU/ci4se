def path_helper(self, path, view, **kwargs):
    super(FlaskRestyPlugin, self).path_helper(path=path, view=view, **kwargs)
    resource = self.get_state().views[view]
    rule = self._rules[resource.rule]
    operations = defaultdict(Operation)
    view_instance = view()
    view_instance.spec_declaration(view, operations, self)
    parameters = []
    for arg in rule.arguments:
        parameters.append({'name': arg, 'in': 'path', 'required': True,
            'type': 'string'})
    if parameters:
        operations['parameters'] = parameters
    path.path = FlaskPlugin.flaskpath2openapi(resource.rule)
    path.operations = dict(**operations)