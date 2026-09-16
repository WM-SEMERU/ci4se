def get_parser():
    parser = argparse.ArgumentParser(allow_abbrev=True, description=
        'pypyr pipeline runner')
    parser.add_argument('pipeline_name', help=
        'Name of pipeline to run. It should exist in the ./pipelines directory.'
        )
    parser.add_argument(dest='pipeline_context', nargs='?', help=
        "String for context values. Parsed by the pipeline's context_parser function."
        )
    parser.add_argument('--dir', dest='working_dir', default=os.getcwd(),
        help=
        'Working directory. Use if your pipelines directory is elsewhere. Defaults to cwd.'
        )
    parser.add_argument('--log', '--loglevel', dest='log_level', type=int,
        default=20, help=
        """Integer log level. Defaults to 20 (INFO). 10=DEBUG
20=INFO
30=WARNING
40=ERROR
50=CRITICAL.
 Log Level < 10 gives full traceback on errors."""
        )
    parser.add_argument('--logpath', dest='log_path', help=
        'Log-file path. Append log output to this path')
    parser.add_argument('--version', action='version', help=
        'Echo version number.', version=f'{pypyr.version.get_version()}')
    return parser