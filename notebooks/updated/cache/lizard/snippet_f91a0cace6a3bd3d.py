def __remove_actions(self):
    LOGGER.debug("> Removing '{0}' Component actions.".format(self.
        __class__.__name__))
    remove_project_action = (
        'Actions|Umbra|Components|factory.script_editor|&File|Remove Project')
    self.__script_editor.command_menu.removeAction(self.__engine.
        actions_manager.get_action(remove_project_action))
    self.__engine.actions_manager.unregister_action(remove_project_action)