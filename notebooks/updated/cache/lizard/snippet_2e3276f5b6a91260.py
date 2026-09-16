def makeParser(self):
    self.parser = argparse.ArgumentParser(description=
        'Starts the executable.', prog='{0} -m scoop.bootstrap'.format(sys.
        executable))
    self.parser.add_argument('--origin', help=
        'To specify that the worker is the origin', action='store_true')
    self.parser.add_argument('--brokerHostname', help=
        'The routable hostname of a broker', default='')
    self.parser.add_argument('--externalBrokerHostname', help=
        'Externally routable hostname of local worker', default='')
    self.parser.add_argument('--taskPort', help=
        'The port of the broker task socket', type=int)
    self.parser.add_argument('--metaPort', help=
        'The port of the broker meta socket', type=int)
    self.parser.add_argument('--size', help='The size of the worker pool',
        type=int, default=1)
    self.parser.add_argument('--nice', help=
        'Adjust the niceness of the process', type=int, default=0)
    self.parser.add_argument('--debug', help='Activate the debug', action=
        'store_true')
    self.parser.add_argument('--profile', help='Activate the profiler',
        action='store_true')
    self.parser.add_argument('--workingDirectory', help=
        'Set the working directory for the execution', default=os.path.
        expanduser('~'))
    self.parser.add_argument('--backend', help=
        'Choice of communication backend', choices=['ZMQ', 'TCP'], default=
        'ZMQ')
    self.parser.add_argument('executable', nargs='?', help=
        'The executable to start with scoop')
    self.parser.add_argument('args', nargs=argparse.REMAINDER, help=
        'The arguments to pass to the executable', default=[])
    self.parser.add_argument('--verbose', '-v', action='count', help=
        'Verbosity level of this launch script(-vv for more)', default=0)