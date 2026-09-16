def create_from_dictionary(self, datas):
    configuration = ObjectConfiguration()
    if 'uri' in datas:
        configuration.uri = str(datas['uri'])
    if 'title' in datas:
        configuration.title = str(datas['title'])
    if 'description' in datas:
        configuration.description = str(datas['description'])
    return configuration