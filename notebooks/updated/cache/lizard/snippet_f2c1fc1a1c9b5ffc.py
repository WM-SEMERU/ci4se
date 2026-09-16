def ParseArguments(self):
    loggers.ConfigureLogging()
    argument_parser = argparse.ArgumentParser(description=self.DESCRIPTION,
        add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter)
    self.AddBasicOptions(argument_parser)
    argument_helper_names = ['storage_file']
    if self._CanEnforceProcessMemoryLimit():
        argument_helper_names.append('process_resources')
    helpers_manager.ArgumentHelperManager.AddCommandLineArguments(
        argument_parser, names=argument_helper_names)
    argument_parser.add_argument('--compare', dest='compare_storage_file',
        type=str, action='store', default='', metavar='STORAGE_FILE', help=
        'The path of the storage file to compare against.')
    argument_parser.add_argument('--output_format', '--output-format', dest
        ='output_format', type=str, choices=['text', 'json'], action=
        'store', default='text', metavar='FORMAT', help=
        'Format of the output, the default is: text. Supported options: json, text.'
        )
    argument_parser.add_argument('-v', '--verbose', dest='verbose', action=
        'store_true', default=False, help='Print verbose output.')
    argument_parser.add_argument('-w', '--write', metavar='OUTPUTFILE',
        dest='write', help='Output filename.')
    try:
        options = argument_parser.parse_args()
    except UnicodeEncodeError:
        self._output_writer.Write('\n')
        self._output_writer.Write(argument_parser.format_help())
        return False
    try:
        self.ParseOptions(options)
    except errors.BadConfigOption as exception:
        self._output_writer.Write('ERROR: {0!s}\n'.format(exception))
        self._output_writer.Write('\n')
        self._output_writer.Write(argument_parser.format_usage())
        return False
    loggers.ConfigureLogging(debug_output=self._debug_mode, filename=self.
        _log_file, quiet_mode=self._quiet_mode)
    return True