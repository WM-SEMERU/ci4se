def new(project_name):
    try:
        locale.setlocale(locale.LC_ALL, '')
    except:
        print('Warning: Unable to set locale.  Expect encoding problems.')
    config = utils.get_config()
    config['new_project']['project_name'] = project_name
    values = new_project_ui(config)
    if type(values) is not str:
        print('New project options:')
        pprint.pprint(values)
        project_dir = render.render_project(**values)
        git.init_repo(project_dir, **values)
    else:
        print(values)