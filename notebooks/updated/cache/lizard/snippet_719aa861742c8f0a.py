def _build_function(self, function_name, codeuri, runtime):
    code_dir = str(pathlib.Path(self._base_dir, codeuri).resolve())
    config = get_workflow_config(runtime, code_dir, self._base_dir)
    artifacts_dir = str(pathlib.Path(self._build_dir, function_name))
    with osutils.mkdir_temp() as scratch_dir:
        manifest_path = self._manifest_path_override or os.path.join(code_dir,
            config.manifest_name)
        build_method = self._build_function_in_process
        if self._container_manager:
            build_method = self._build_function_on_container
        return build_method(config, code_dir, artifacts_dir, scratch_dir,
            manifest_path, runtime)