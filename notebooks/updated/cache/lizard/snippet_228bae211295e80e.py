def _SeparateTypes(self, metadata_value_pairs):
    registry_pairs = []
    file_pairs = []
    match_pairs = []
    for metadata, result in metadata_value_pairs:
        if (result.stat_entry.pathspec.pathtype == rdf_paths.PathSpec.
            PathType.REGISTRY):
            registry_pairs.append((metadata, result.stat_entry))
        else:
            file_pairs.append((metadata, result))
        match_pairs.extend([(metadata, match) for match in result.matches])
    return registry_pairs, file_pairs, match_pairs