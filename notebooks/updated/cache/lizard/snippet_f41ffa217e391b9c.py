def generate_docker_targets():
    output = {}
    for py_ver in python_versions.values():
        filepath = os.path.join(container_config_root, py_ver.docker_file)
        output[filepath] = generate_docker_file(py_ver)
        filepath = os.path.join(container_config_root, py_ver.compose_file)
        output[filepath] = generate_compose_file(py_ver)
    return output