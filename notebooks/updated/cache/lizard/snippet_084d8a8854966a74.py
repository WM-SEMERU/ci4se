def build_image_here(source, image, parent_registry=None, target_registries
    =None, parent_registry_insecure=False, target_registries_insecure=False,
    dont_pull_base_image=False, **kwargs):
    build_json = _prepare_build_json(image, source, parent_registry,
        target_registries, parent_registry_insecure,
        target_registries_insecure, dont_pull_base_image, **kwargs)
    m = DockerBuildWorkflow(**build_json)
    return m.build_docker_image()