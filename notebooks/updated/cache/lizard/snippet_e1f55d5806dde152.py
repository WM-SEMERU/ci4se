def from_name(api_url, name, dry_run=False):
    return DataSet('/'.join([api_url, name]).rstrip('/'), token=None,
        dry_run=dry_run)