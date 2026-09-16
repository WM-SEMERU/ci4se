def main():
    run_config = _parse_args(sys.argv[1:])
    if run_config.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    gitlab_config = GitLabConfig(run_config.url, run_config.token)
    project_updater_builder = FileBasedProjectVariablesUpdaterBuilder(
        setting_repositories=run_config.setting_repositories,
        default_setting_extensions=run_config.default_setting_extensions)
    updater = FileBasedProjectsVariablesUpdater(config_location=run_config.
        config_location, gitlab_config=gitlab_config,
        project_variables_updater_builder=project_updater_builder)
    updater.update()