def register_actions(self, shortcut_manager):
    super(DescriptionEditorController, self).register_actions(shortcut_manager)
    shortcut_manager.add_callback_for_action('abort', self._abort)