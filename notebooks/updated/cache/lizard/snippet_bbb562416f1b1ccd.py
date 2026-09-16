def close(self):
    try:
        super(DockerFabricClient, self).close()
    finally:
        if self._tunnel is not None:
            self._tunnel.close()