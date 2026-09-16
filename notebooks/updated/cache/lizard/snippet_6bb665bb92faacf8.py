def docker_context():
    try:
        client = docker.from_env(version='auto', timeout=int(os.environ.get
            ('DOCKER_CLIENT_TIMEOUT', 180)), assert_hostname=False)
        info = client.info()
        log.info('Connected to docker daemon\tdriver=%s\tkernel=%s', info[
            'Driver'], info['KernelVersion'])
    except (DockerException, APIError) as error:
        raise BadDockerConnection(error=error)
    return client