def update_fmt_with_notebook_options(self, metadata):
    for opt in _VALID_FORMAT_OPTIONS:
        if opt in metadata.get('jupytext', {}):
            self.fmt.setdefault(opt, metadata['jupytext'][opt])
        if opt in self.fmt:
            metadata.setdefault('jupytext', {}).setdefault(opt, self.fmt[opt])
    if metadata.get('jupytext', {}).get('rst2md') is True:
        metadata['jupytext']['rst2md'] = False