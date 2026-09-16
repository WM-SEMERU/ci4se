def context(root, project=''):
    environment = os.environ.copy()
    environment.update({'BE_PROJECT': project, 'BE_PROJECTROOT': os.path.
        join(root, project).replace('\\', '/') if project else '',
        'BE_PROJECTSROOT': root, 'BE_ALIASDIR': '', 'BE_CWD': root, 'BE_CD':
        '', 'BE_ROOT': '', 'BE_TOPICS': '', 'BE_DEVELOPMENTDIR': '',
        'BE_ACTIVE': '1', 'BE_USER': '', 'BE_SCRIPT': '', 'BE_PYTHON': '',
        'BE_ENTER': '', 'BE_TEMPDIR': '', 'BE_PRESETSDIR': '',
        'BE_GITHUB_API_TOKEN': '', 'BE_ENVIRONMENT': '', 'BE_BINDING': '',
        'BE_TABCOMPLETION': ''})
    return environment