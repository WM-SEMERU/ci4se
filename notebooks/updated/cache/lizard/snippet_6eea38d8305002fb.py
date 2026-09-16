def _register_pyflakes_check():
    from flake8_isort import Flake8Isort
    from flake8_blind_except import check_blind_except
    codes = {'UnusedImport': 'F401', 'ImportShadowedByLoopVar': 'F402',
        'ImportStarUsed': 'F403', 'LateFutureImport': 'F404', 'Redefined':
        'F801', 'RedefinedInListComp': 'F812', 'UndefinedName': 'F821',
        'UndefinedExport': 'F822', 'UndefinedLocal': 'F823',
        'DuplicateArgument': 'F831', 'UnusedVariable': 'F841'}
    for name, obj in vars(pyflakes.messages).items():
        if name[0].isupper() and obj.message:
            obj.tpl = '{0} {1}'.format(codes.get(name, 'F999'), obj.message)
    pep8.register_check(_PyFlakesChecker, codes=['F'])
    parser = pep8.get_parser('', '')
    Flake8Isort.add_options(parser)
    options, args = parser.parse_args([])
    pep8.register_check(Flake8Isort, codes=['I'])
    pep8.register_check(check_blind_except, codes=['B90'])