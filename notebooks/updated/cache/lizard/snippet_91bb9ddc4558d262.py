def __load_settings_from_file(self):
    filename = self.get_base_path() + 'settings.json'
    if not exists(filename):
        raise OneLogin_Saml2_Error('Settings file not found: %s',
            OneLogin_Saml2_Error.SETTINGS_FILE_NOT_FOUND, filename)
    with open(filename, 'r') as json_data:
        settings = json.loads(json_data.read())
    advanced_filename = self.get_base_path() + 'advanced_settings.json'
    if exists(advanced_filename):
        with open(advanced_filename, 'r') as json_data:
            settings.update(json.loads(json_data.read()))
    return self.__load_settings_from_dict(settings)