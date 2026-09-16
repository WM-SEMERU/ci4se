def add_distdiff_optgroup(parser):
    cpus = cpu_count()
    og = parser.add_argument_group('Distribution Checking Options')
    og.add_argument('--processes', type=int, default=cpus, help=
        'Number of child processes to spawn to handle sub-reports. Set to 0 to disable multi-processing. Defaults to the number of CPUs (%r)'
         % cpus)
    og.add_argument('--shallow', action='store_true', default=False, help=
        'Check only that the files of this dist havechanged, do not infer the meaning'
        )
    og.add_argument('--ignore-filenames', action='append', default=[], help
        ='file glob to ignore. Can be specified multiple times')
    og.add_argument('--ignore-trailing-whitespace', action='store_true',
        default=False, help=
        'ignore trailing whitespace when comparing text files')