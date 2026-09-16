def linkify(self, commands, notificationways):
    self.linkify_with_notificationways(notificationways)
    self.linkify_command_list_with_commands(commands,
        'service_notification_commands')
    self.linkify_command_list_with_commands(commands,
        'host_notification_commands')