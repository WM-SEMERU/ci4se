def activate_components_ui(self):
    selected_components = self.get_selected_components()
    self.__engine.start_processing('Activating Components ...', len(
        selected_components))
    activation_failed_components = []
    for component in selected_components:
        if not component.interface.activated:
            success = self.activate_component(component.name) or False
            if not success:
                activation_failed_components.append(component)
        else:
            self.__engine.notifications_manager.warnify(
                "{0} | '{1}' Component is already activated!".format(self.
                __class__.__name__, component.name))
        self.__engine.step_processing()
    self.__engine.stop_processing()
    self.__store_deactivated_components()
    if not activation_failed_components:
        return True
    else:
        raise manager.exceptions.ComponentActivationError(
            "{0} | Exception(s) raised while activating '{1}' Component(s)!"
            .format(self.__class__.__name__, ', '.join(
            activation_failed_component.name for
            activation_failed_component in activation_failed_components)))