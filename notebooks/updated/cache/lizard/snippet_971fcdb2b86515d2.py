def load_config(self):
    self.__config = {}
    for section in self.sections:
        self.__config[section] = {}
        options = self.parser.options(section)
        for option in options:
            try:
                opt = self.parser.get(section, option)
                try:
                    self.__config[section][option] = literal_eval(opt)
                except (SyntaxError, ValueError):
                    self.__config[section][option] = opt
                    self.log_output.append({'level': 'debug', 'msg':
                        'Option not literal_eval-parsable (maybe string): [{0}] {1}'
                        .format(section, option)})
                if self.__config[section][option] == -1:
                    self.log_output.append({'level': 'debug', 'msg': 
                        'Skipping: [%s] %s' % (section, option)})
            except ConfigParser.NoOptionError as exc:
                self.log_output.append({'level': 'error', 'msg': 
                    'Exception on [%s] %s: %s' % (section, option, exc)})
                self.__config[section][option] = None