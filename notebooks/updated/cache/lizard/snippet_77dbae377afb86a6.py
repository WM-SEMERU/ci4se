def _MatchPath(self, pathspec, response):
    to_match = response.pathspec.Basename()
    if pathspec.path_options == rdf_paths.PathSpec.Options.CASE_INSENSITIVE:
        return to_match.lower() == pathspec.path.lower()
    elif pathspec.path_options == rdf_paths.PathSpec.Options.CASE_LITERAL:
        return to_match == pathspec.path
    elif pathspec.path_options == rdf_paths.PathSpec.Options.REGEX:
        return bool(re.match(pathspec.path, to_match, flags=re.IGNORECASE))
    elif pathspec.path_options == rdf_paths.PathSpec.Options.RECURSIVE:
        return True
    raise ValueError('Unknown Pathspec type.')