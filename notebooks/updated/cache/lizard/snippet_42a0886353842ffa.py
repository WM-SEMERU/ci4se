def get_ecosystem_solver(ecosystem_name, parser_kwargs=None, fetcher_kwargs
    =None):
    from .python import PythonSolver
    if ecosystem_name.lower() == 'pypi':
        source = Source(url='https://pypi.org/simple', warehouse_api_url=
            'https://pypi.org/pypi', warehouse=True)
        return PythonSolver(parser_kwargs, fetcher_kwargs={'source': source})
    raise NotImplementedError('Unknown ecosystem: {}'.format(ecosystem_name))