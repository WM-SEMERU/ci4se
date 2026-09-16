def _get_help_names(self):
    help_names = {}
    token2cmdname = self._get_canonical_map()
    for attrname, attr in self._gen_names_and_attrs():
        if not attrname.startswith('help_'):
            continue
        help_name = attrname[5:]
        if help_name not in token2cmdname:
            help_names[help_name] = attr
    return help_names