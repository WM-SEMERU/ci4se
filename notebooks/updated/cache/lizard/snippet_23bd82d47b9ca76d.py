def _deferred_blueprint_init(self, setup_state):
    self.blueprint_setup = setup_state
    if setup_state.add_url_rule.__name__ != '_add_url_rule_patch':
        setup_state._original_add_url_rule = setup_state.add_url_rule
        setup_state.add_url_rule = MethodType(Api._add_url_rule_patch,
            setup_state)
    if not setup_state.first_registration:
        raise ValueError(
            'flask-RESTEasy blueprints can only be registered once.')
    self._init_app(setup_state.app)