def _create_more_application():
    from prompt_toolkit.shortcuts import create_prompt_application
    registry = Registry()

    @registry.add_binding(' ')
    @registry.add_binding('y')
    @registry.add_binding('Y')
    @registry.add_binding(Keys.ControlJ)
    @registry.add_binding(Keys.ControlI)
    def _(event):
        event.cli.set_return_value(True)

    @registry.add_binding('n')
    @registry.add_binding('N')
    @registry.add_binding('q')
    @registry.add_binding('Q')
    @registry.add_binding(Keys.ControlC)
    def _(event):
        event.cli.set_return_value(False)
    return create_prompt_application('--MORE--', key_bindings_registry=
        registry, erase_when_done=True)