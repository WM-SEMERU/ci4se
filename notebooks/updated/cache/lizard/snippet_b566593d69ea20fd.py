def notify_server_ready(self, language, config):
    for index in range(self.get_stack_count()):
        editor = self.tabs.widget(index)
        if editor.language.lower() == language:
            editor.start_lsp_services(config)