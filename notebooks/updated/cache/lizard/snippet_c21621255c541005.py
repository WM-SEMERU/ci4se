def copy_resource(self, container, resource, local_filename):
    self.push_log("Receiving tarball for resource '{0}:{1}' and storing as {2}"
        .format(container, resource, local_filename))
    super(DockerFabricClient, self).copy_resource(container, resource,
        local_filename)