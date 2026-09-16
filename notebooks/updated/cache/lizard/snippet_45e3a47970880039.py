def GetUrnHashEntry(urn, token=None):
    if data_store.RelationalDBEnabled():
        client_id, vfs_path = urn.Split(2)
        path_type, components = rdf_objects.ParseCategorizedPath(vfs_path)
        path_info = data_store.REL_DB.ReadPathInfo(client_id, path_type,
            components)
        return path_info.hash_entry
    else:
        with aff4.FACTORY.Open(urn, token=token) as fd:
            return GetFileHashEntry(fd)