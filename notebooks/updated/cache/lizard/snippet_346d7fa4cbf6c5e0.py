def get_plugin_client_settings(self):
    settings = {}
    user_path = self.get_plugin_settings_path('User')
    def_path = self.get_plugin_settings_path('MavensMate')
    if def_path == None:
        if 'ATOM' in self.plugin_client:
            file_name = 'atom'
        elif 'SUBLIME_TEXT' in self.plugin_client:
            file_name = 'st3'
        elif 'BRACKETS' in self.plugin_client:
            file_name = 'brackets'
        settings['default'] = util.parse_json_from_file(config.base_path +
            '/' + config.support_dir + '/config/' + file_name + '.json')
        if config.plugin_client_settings != None:
            settings['user'] = config.plugin_client_settings
    else:
        workspace = self.params.get('workspace', None)
        if self.project_name != None and workspace != None:
            try:
                settings['project'] = util.parse_json_from_file(os.path.
                    join(workspace, self.project_name, self.project_name +
                    '.sublime-settings'))
            except:
                debug('Project settings could not be loaded')
        if not user_path == None:
            try:
                settings['user'] = util.parse_json_from_file(user_path)
            except:
                debug('User settings could not be loaded')
        if not def_path == None:
            try:
                settings['default'] = util.parse_json_from_file(def_path)
            except:
                raise MMException('Could not load default MavensMate settings.'
                    )
    if settings == {}:
        raise MMException(
            'Could not load MavensMate settings. Please ensure they contain valid JSON'
            )
    return settings