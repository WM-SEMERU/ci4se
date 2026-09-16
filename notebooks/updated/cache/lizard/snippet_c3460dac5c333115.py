def project_transfer_config_path(cls, project, transfer_config):
    return google.api_core.path_template.expand(
        'projects/{project}/transferConfigs/{transfer_config}', project=
        project, transfer_config=transfer_config)