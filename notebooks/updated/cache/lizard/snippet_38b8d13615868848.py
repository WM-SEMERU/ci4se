def Parse(self, persistence, knowledge_base, download_pathtype):
    pathspecs = []
    if isinstance(persistence, rdf_client.WindowsServiceInformation):
        if persistence.HasField('binary'):
            pathspecs.append(persistence.binary.pathspec)
        elif persistence.HasField('image_path'):
            pathspecs = self._GetFilePaths(persistence.image_path,
                download_pathtype, knowledge_base)
    if isinstance(persistence, rdf_client_fs.StatEntry
        ) and persistence.HasField('registry_type'):
        pathspecs = self._GetFilePaths(persistence.registry_data.string,
            download_pathtype, knowledge_base)
    for pathspec in pathspecs:
        yield rdf_standard.PersistenceFile(pathspec=pathspec)