def package_releases(self, package_name):
    if self.debug:
        self.logger.debug('DEBUG: querying PyPI for versions of ' +
            package_name)
    return self.xmlrpc.package_releases(package_name)