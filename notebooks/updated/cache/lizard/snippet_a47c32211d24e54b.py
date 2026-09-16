def create_build_configuration_process(repository, revision, **kwargs):
    if not kwargs.get('dependency_ids'):
        kwargs['dependency_ids'] = []
    if not kwargs.get('build_configuration_set_ids'):
        kwargs['build_configuration_set_ids'] = []
    if kwargs.get('generic_parameters'):
        kwargs['generic_parameters'] = ast.literal_eval(kwargs.get(
            'generic_parameters'))
    if not kwargs.get('project'):
        kwargs['project'] = pnc_api.projects.get_specific(kwargs.get(
            'project_id')).content
    if not kwargs.get('environment'):
        kwargs['environment'] = pnc_api.environments.get_specific(kwargs.
            get('build_environment_id')).content
    build_configuration = create_build_conf_object(scm_revision=revision,
        **kwargs)
    repo_creation = swagger_client.RepositoryCreationUrlAutoRest()
    repo_creation.scm_url = repository
    repo_creation.build_configuration_rest = build_configuration
    response = utils.checked_api_call(pnc_api.bpm,
        'start_r_creation_task_with_single_url', body=repo_creation)
    if response:
        return response