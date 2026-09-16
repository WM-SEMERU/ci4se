def check_if_exists(self):
    if self.req is None:
        return False
    try:
        self.satisfied_by = pkg_resources.get_distribution(self.req)
    except pkg_resources.DistributionNotFound:
        return False
    except pkg_resources.VersionConflict:
        self.conflicts_with = pkg_resources.get_distribution(self.req.
            project_name)
    return True