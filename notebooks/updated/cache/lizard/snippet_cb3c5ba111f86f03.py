def config_maker(project_name, path):
    with open(skeleton_path('config.py'), 'r') as config_source:
        config_content = config_source.read()
    config_content = config_content.replace('__PROJECT_NAME__', project_name)
    with open(path, 'w') as config_dest:
        config_dest.write(config_content)