def _init_qualifier(qualifier, qual_repo):
    qual_dict_entry = qual_repo[qualifier.name]
    qualifier.propagated = False
    if qualifier.tosubclass is None:
        if qual_dict_entry.tosubclass is None:
            qualifier.tosubclass = True
        else:
            qualifier.tosubclass = qual_dict_entry.tosubclass
    if qualifier.overridable is None:
        if qual_dict_entry.overridable is None:
            qualifier.overridable = True
        else:
            qualifier.overridable = qual_dict_entry.overridable
    if qualifier.translatable is None:
        qualifier.translatable = qual_dict_entry.translatable