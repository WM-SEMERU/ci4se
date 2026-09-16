def __add_actions(self):
    LOGGER.debug("> Adding '{0}' Component actions.".format(self.__class__.
        __name__))
    self.__script_editor.command_menu.addSeparator()
    self.__script_editor.command_menu.addAction(self.__engine.
        actions_manager.register_action(
        'Actions|Umbra|Components|addons.tcp_serverUi|&Command|Send Selection To Server'
        , shortcut=Qt.ControlModifier + Qt.AltModifier + Qt.Key_Return,
        slot=self.__send_selection_to_server_action__triggered))
    self.__script_editor.command_menu.addAction(self.__engine.
        actions_manager.register_action(
        'Actions|Umbra|Components|addons.tcp_serverUi|&Command|&Send Current File To Server'
        , shortcut=Qt.SHIFT + Qt.AltModifier + Qt.CTRL + Qt.Key_Return,
        slot=self.__send_file_to_server_action__triggered))