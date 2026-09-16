def install_package(self, client, package):
    try:
        out = self.distro.install_package(client, package)
    except Exception as error:
        raise IpaCloudException('Failed installing package, "{0}"; {1}.'.
            format(package, error))
    else:
        self._write_to_log(out)