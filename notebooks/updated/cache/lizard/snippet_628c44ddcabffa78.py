def __set_folder_list(self, section):
    for l in range(1, self.__folder_list_max_size + 1):
        value = {}
        key = 'folder_' + str(l) + '_'
        value['indice'] = str(l)
        value['path'] = self.config.get_value(section, key + 'path')
        if value['path'] is None:
            continue
        else:
            value['path'] = nativestr(value['path'])
        for i in ['careful', 'warning', 'critical']:
            value[i] = self.config.get_value(section, key + i)
            if value[i] is not None:
                logger.debug('{} threshold for folder {} is {}'.format(i,
                    value['path'], value[i]))
            action = self.config.get_value(section, key + i + '_action')
            if action is not None:
                value[i + '_action'] = action
                logger.debug('{} action for folder {} is {}'.format(i,
                    value['path'], value[i + '_action']))
        self.__folder_list.append(value)