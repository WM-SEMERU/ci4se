def copy(self, repository=None, tag=None, source_transport=None,
    target_transport=SkopeoTransport.DOCKER, source_path=None, target_path=
    None, logs=True):
    if not repository:
        repository = self.name
    if not tag:
        tag = self.tag if self.tag else 'latest'
    if target_transport == SkopeoTransport.OSTREE and tag and logs:
        logging.warning('tag was ignored')
    target = DockerImage(repository, tag, pull_policy=DockerImagePullPolicy
        .NEVER).using_transport(target_transport, target_path)
    self.using_transport(source_transport, source_path)
    try:
        run_cmd(['skopeo', 'copy', transport_param(self), transport_param(
            target)])
    except subprocess.CalledProcessError:
        raise ConuException('There was an error while copying repository',
            self.name)
    return target