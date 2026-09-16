def setup_subparser(self, func=None, setup_as=None, insert_at=None,
    interprete=True, epilog_sections=None, overwrite=False, append_epilog=
    True, return_parser=False, name=None, **kwargs):

    def setup(func):
        if self._subparsers_action is None:
            raise RuntimeError(
                'No subparsers have yet been created! Run the add_subparsers method first!'
                )
        name2use = name
        if name2use is None:
            name2use = func.__name__.replace('_', '-')
        kwargs.setdefault('help', docstrings.get_summary(docstrings.dedents
            (inspect.getdoc(func))))
        parser = self._subparsers_action.add_parser(name2use, **kwargs)
        parser.setup_args(func, setup_as=setup_as, insert_at=insert_at,
            interprete=interprete, epilog_sections=epilog_sections,
            overwrite=overwrite, append_epilog=append_epilog)
        return func, parser
    if func is None:
        return lambda f: setup(f)[0]
    else:
        return setup(func)[int(return_parser)]