def relative_resources(pathstring, failover='nifstd/resources'):
    if working_dir is None:
        return Path(failover, pathstring).resolve()
    else:
        return Path(devconfig.resources, pathstring).resolve().relative_to(
            working_dir.resolve())