def add_custom_options(parser):
    parser.add_argument('--report-title', type=str, metavar='TITLE',
        default='Genetic Data Clean Up', help=
        'The report title. [default: %(default)s]')
    parser.add_argument('--report-author', type=str, metavar='AUTHOR',
        default='pyGenClean', help=
        'The current project number. [default: %(default)s]')
    parser.add_argument('--report-number', type=str, metavar='NUMBER',
        default='Simple Project', help=
        'The current project author. [default: %(default)s]')
    parser.add_argument('--report-background', type=str, metavar=
        'BACKGROUND', default=
        'The aim of this project is to perform data QC prior to genetic analysis.'
        , help='Text of file containing the background section of the report.')