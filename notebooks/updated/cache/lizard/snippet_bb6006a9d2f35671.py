def __get_supported_file_types_string(self):
    languages = ['All Files (*)']
    for language in self.__languages_model.languages:
        languages.append('{0} Files ({1})'.format(language.name, ' '.join(
            language.extensions.split('|')).replace('\\', '*')))
    return ';;'.join(languages)