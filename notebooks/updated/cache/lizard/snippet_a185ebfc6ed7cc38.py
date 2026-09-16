def main():
    parser = argparse.ArgumentParser(description=
        'Monitor your crons with cronitor.io & sentry.io', epilog=
        'https://github.com/youversion/crony', prog='crony')
    parser.add_argument('-c', '--cronitor', action='store', help=
        'Cronitor link identifier. This can be found in your Cronitor unique ping URL right after https://cronitor.link/'
        )
    parser.add_argument('-e', '--venv', action='store', help=
        'Path to virtualenv to source before running script. May be passed as an argument or loaded from an environment variable or config file.'
        )
    parser.add_argument('-d', '--cd', action='store', help=
        'If the script needs ran in a specific directory, than can be passed or cd can be ran prior to running crony.'
        )
    parser.add_argument('-l', '--log', action='store', help=
        'Log file to direct stdout of script run to. Can be passed or defined in config file with "log_file"'
        )
    parser.add_argument('-o', '--config', action='store', help=
        'Path to a crony config file to use.')
    parser.add_argument('-p', '--path', action='store', help=
        'Paths to append to the PATH environment variable before running.  Can be passed as an argument or loaded from config file.'
        )
    parser.add_argument('-s', '--dsn', action='store', help=
        'Sentry DSN. May be passed or loaded from an environment variable or a config file.'
        )
    parser.add_argument('-t', '--timeout', action='store', default=10, help
        ='Timeout to use when sending requests to Cronitor', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', help=
        'Increase level of verbosity output by crony')
    parser.add_argument('--version', action='store_true', help=
        'Output crony version # and exit')
    parser.add_argument('cmd', nargs=argparse.REMAINDER, help=
        'Command to run and monitor')
    cc = CommandCenter(parser.parse_args())
    sys.exit(cc.log(*cc.func()))