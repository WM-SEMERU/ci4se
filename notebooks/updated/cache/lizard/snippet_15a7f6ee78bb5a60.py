def __update_paths(self, settings):
    if not isinstance(settings, dict):
        return
    if 'custom_base_path' in settings:
        base_path = settings['custom_base_path']
        base_path = join(dirname(__file__), base_path)
        self.__load_paths(base_path)