def GetArtifactPathDependencies(rdf_artifact):
    deps = set()
    for source in rdf_artifact.sources:
        for arg, value in iteritems(source.attributes):
            paths = []
            if arg in ['path', 'query']:
                paths.append(value)
            if arg == 'key_value_pairs':
                paths.extend([x['key'] for x in value])
            if arg in ['keys', 'paths', 'path_list', 'content_regex_list']:
                paths.extend(value)
            for path in paths:
                for match in artifact_utils.INTERPOLATED_REGEX.finditer(path):
                    deps.add(match.group()[2:-2])
    deps.update(GetArtifactParserDependencies(rdf_artifact))
    return deps