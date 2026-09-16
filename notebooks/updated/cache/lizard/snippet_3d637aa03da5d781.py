def options(self, parser, env):
    Plugin.options(self, parser, env)
    parser.add_option('--html-file', action='store', dest='html_file',
        metavar='FILE', default=env.get('NOSE_HTML_FILE', 'nosetests.html'),
        help=
        'Path to html file to store the report in. Default is nosetests.html in the working directory [NOSE_HTML_FILE]'
        )