def create_asset(json):
    result = Asset(json['sys'])
    file_dict = json['fields']['file']
    result.fields = json['fields']
    result.url = file_dict['url']
    result.mimeType = file_dict['contentType']
    return result