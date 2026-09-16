def new(path='.', template=None):
    path = abspath(path.rstrip(sep))
    template = template or DEFAULT_TEMPLATE_URL
    render_skeleton(template, path, include_this=['.gitignore'],
        filter_this=['~*', '*.py[co]', '__pycache__', '__pycache__/*',
        '.git', '.git/*', '.hg', '.hg/*', '.svn', '.svn/*'])
    print(HELP_MSG % (path,))