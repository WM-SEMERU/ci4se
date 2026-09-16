def resource_type(self, resource_id):
    match = re.search('repositories/\\d+/(resources|archival_objects)/\\d+',
        resource_id)
    if match and match.groups():
        type_ = match.groups()[0]
        return 'resource' if type_ == 'resources' else 'resource_component'
    else:
        raise ArchivesSpaceError('Unable to determine type of provided ID: {}'
            .format(resource_id))