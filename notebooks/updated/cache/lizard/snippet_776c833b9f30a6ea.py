def preferred_jvm_distribution(cls, platforms, strict=False):
    if not platforms:
        return DistributionLocator.cached()
    min_version = max(platform.target_level for platform in platforms)
    max_version = Revision(*(min_version.components + [9999])
        ) if strict else None
    return DistributionLocator.cached(minimum_version=min_version,
        maximum_version=max_version)