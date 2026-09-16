def iter_records_for(self, package_name):
    entry_points = self.packages.get(package_name, NotImplemented)
    if entry_points is NotImplemented:
        logger.debug(
            "package '%s' has not declared any entry points for the '%s' registry for artifact construction"
            , package_name, self.registry_name)
        return iter([])
    logger.debug(
        "package '%s' has declared %d entry points for the '%s' registry for artifact construction"
        , package_name, len(entry_points), self.registry_name)
    return iter(entry_points.values())