def AddArguments(cls, argument_group):
    argument_group.add_argument('--analysis', metavar='PLUGIN_LIST', dest=
        'analysis_plugins', default='', action='store', type=str, help=
        'A comma separated list of analysis plugin names to be loaded or "--analysis list" to see a list of available plugins.'
        )
    arguments = sys.argv[1:]
    argument_index = 0
    if '--analysis' in arguments:
        argument_index = arguments.index('--analysis') + 1
    if 0 < argument_index < len(arguments):
        names = [name.strip() for name in arguments[argument_index].split(',')]
    else:
        names = None
    if names and names != ['list']:
        manager.ArgumentHelperManager.AddCommandLineArguments(argument_group,
            category='analysis', names=names)