def builder_from_source(source, filename, system_includes,
    nonsystem_includes, quiet=False):
    return ASTBuilder(tokenize.get_tokens(source), filename,
        system_includes, nonsystem_includes, quiet=quiet)