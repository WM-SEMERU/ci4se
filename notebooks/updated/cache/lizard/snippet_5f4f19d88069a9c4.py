def CollectionItemToClientPath(item, client_id=None):
    if isinstance(item, rdf_flows.GrrMessage):
        client_id = item.source
        item = item.payload
    elif isinstance(item, rdf_flow_objects.FlowResult):
        client_id = item.client_id
        item = item.payload
    if client_id is None:
        raise ValueError('Could not determine client_id.')
    elif isinstance(client_id, rdfvalue.RDFURN):
        client_id = client_id.Basename()
    if isinstance(item, rdf_client_fs.StatEntry):
        return db.ClientPath.FromPathSpec(client_id, item.pathspec)
    elif isinstance(item, rdf_file_finder.FileFinderResult):
        return db.ClientPath.FromPathSpec(client_id, item.stat_entry.pathspec)
    elif isinstance(item, collectors.ArtifactFilesDownloaderResult):
        if item.HasField('downloaded_file'):
            return db.ClientPath.FromPathSpec(client_id, item.
                downloaded_file.pathspec)
    raise ItemNotExportableError(item)