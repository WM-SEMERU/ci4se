def get_project_details(project):
    result = []
    for datastore in _get_datastores():
        value = datastore.get_project_details(project)
        value['datastore'] = datastore.config['DESCRIPTION']
        result.append(value)
    return result