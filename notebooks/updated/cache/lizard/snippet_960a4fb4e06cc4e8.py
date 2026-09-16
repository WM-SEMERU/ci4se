def _init_qualifier_decl(qualifier_decl, qual_repo):
    assert qualifier_decl.name not in qual_repo
    if qualifier_decl.tosubclass is None:
        qualifier_decl.tosubclass = True
    if qualifier_decl.overridable is None:
        qualifier_decl.overridable = True
    if qualifier_decl.translatable is None:
        qualifier_decl.translatable = False