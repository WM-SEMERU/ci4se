def parse_option(self, option, block_name, *values):
    if option == 'run':
        option = 'start_' + option
    key = option.split('_', 1)[0]
    self.paths[key] = set(common.extract_app_paths(values))