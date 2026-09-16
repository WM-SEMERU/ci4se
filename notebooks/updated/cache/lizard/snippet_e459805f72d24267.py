def generate_travis_yml():

    def get_mustache_file(file_name):
        return pkg_resources.resource_string(__name__, file_name).decode(
            'utf-8')
    template = get_mustache_file('travis.yml.mustache')
    before_install_linux = get_mustache_file('before_install_linux.mustache')
    before_install_osx = get_mustache_file('before_install_osx.mustache')
    env_osx_with_pyenv = get_mustache_file('env_osx_with_pyenv.mustache')
    docker_build_image = get_mustache_file('docker_build_image.mustache')
    docker_run_image = get_mustache_file('docker_run_image.mustache')
    context = {'header': HEADER, 'integration_shards': range(0,
        num_integration_shards), 'integration_shards_length':
        num_integration_shards}
    renderer = pystache.Renderer(partials={'before_install_linux':
        before_install_linux, 'before_install_osx': before_install_osx,
        'env_osx_with_pyenv': env_osx_with_pyenv, 'docker_build_image':
        docker_build_image, 'docker_run_image': docker_run_image})
    print(renderer.render(template, context))