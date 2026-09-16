def _create_project(config):
    try:
        response = config.pbclient.create_project(config.project['name'],
            config.project['short_name'], config.project['description'])
        check_api_error(response)
        return 'Project: %s created!' % config.project['short_name']
    except exceptions.ConnectionError:
        return ('Connection Error! The server %s is not responding' %
            config.server)
    except (ProjectNotFound, TaskNotFound):
        raise