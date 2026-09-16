def node_dependencies(context: Context):
    args = ['--loglevel', {(0): 'silent', (1): 'warn', (2): 'info'}[context
        .verbosity]]
    if not context.use_colour:
        args.append('--color false')
    args.append('install')
    return context.shell('npm', *args)