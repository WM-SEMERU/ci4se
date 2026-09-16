def call_env_updated(cls, kb_app, sphinx_app: Sphinx, sphinx_env:
    BuildEnvironment):
    for callback in EventAction.get_callbacks(kb_app, SphinxEvent.EU):
        callback(kb_app, sphinx_app, sphinx_env)