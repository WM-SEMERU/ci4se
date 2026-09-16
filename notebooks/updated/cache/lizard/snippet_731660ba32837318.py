def parse_opt(self):
    optparser = optparse.OptionParser()
    optparser.add_option('-c', '--config', action='store', dest='config',
        type='string', default='experiments.cfg', help=
        'your experiments config file')
    optparser.add_option('-n', '--numcores', action='store', dest='ncores',
        type='int', default=cpu_count(), help=
        'number of processes you want to use, default is %i' % cpu_count())
    optparser.add_option('-d', '--del', action='store_true', dest='delete',
        default=False, help='delete experiment folder if it exists')
    optparser.add_option('-e', '--experiment', action='append', dest=
        'experiments', type='string', help=
        'run only selected experiments, by default run all experiments in config file.'
        )
    optparser.add_option('-b', '--browse', action='store_true', dest=
        'browse', default=False, help='browse existing experiments.')
    optparser.add_option('-B', '--Browse', action='store_true', dest=
        'browse_big', default=False, help=
        'browse existing experiments, more verbose than -b')
    optparser.add_option('-p', '--progress', action='store_true', dest=
        'progress', default=False, help=
        'like browse, but only shows name and progress bar')
    options, args = optparser.parse_args()
    self.options = options
    return options, args