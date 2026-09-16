def get_options_menu(self):
    env_action = create_action(self, _('Show environment variables'), icon=
        ima.icon('environ'), triggered=self.shellwidget.get_env)
    syspath_action = create_action(self, _('Show sys.path contents'), icon=
        ima.icon('syspath'), triggered=self.shellwidget.get_syspath)
    self.show_time_action.setChecked(self.show_elapsed_time)
    additional_actions = [MENU_SEPARATOR, env_action, syspath_action, self.
        show_time_action]
    if self.menu_actions is not None:
        console_menu = self.menu_actions + additional_actions
        return console_menu
    else:
        return additional_actions