def is_subdomain_zonefile_hash(fqn, zonefile_hash, db_path=None,
    zonefiles_dir=None):
    opts = get_blockstack_opts()
    if not is_subdomains_enabled(opts):
        return []
    if db_path is None:
        db_path = opts['subdomaindb_path']
    if zonefiles_dir is None:
        zonefiles_dir = opts['zonefiles']
    db = SubdomainDB(db_path, zonefiles_dir)
    zonefile_hashes = db.is_subdomain_zonefile_hash(fqn, zonefile_hash)
    return zonefile_hashes