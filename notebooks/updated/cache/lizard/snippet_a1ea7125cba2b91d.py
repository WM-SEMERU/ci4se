def report_open_file(self, options):
    filename = options['filename']
    logger.debug('Call LSP for %s' % filename)
    language = options['language']
    callback = options['codeeditor']
    stat = self.main.lspmanager.start_client(language.lower())
    self.main.lspmanager.register_file(language.lower(), filename, callback)
    if stat:
        if language.lower() in self.lsp_editor_settings:
            self.lsp_server_ready(language.lower(), self.
                lsp_editor_settings[language.lower()])
        else:
            editor = self.get_current_editor()
            editor.lsp_ready = False