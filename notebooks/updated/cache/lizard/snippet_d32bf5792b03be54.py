def _load_generic(packname, package, section, target):
    from acorn.config import settings
    spack = settings(packname)
    if spack.has_section(section):
        secitems = dict(spack.items(section))
        for fqdn, active in secitems.items():
            target[fqdn] = active == '1'