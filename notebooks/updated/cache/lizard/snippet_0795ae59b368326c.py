def get_default_project_directory():
    server_config = Config.instance().get_section_config('Server')
    path = os.path.expanduser(server_config.get('projects_path',
        '~/GNS3/projects'))
    path = os.path.normpath(path)
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        raise aiohttp.web.HTTPInternalServerError(text=
            'Could not create project directory: {}'.format(e))
    return path