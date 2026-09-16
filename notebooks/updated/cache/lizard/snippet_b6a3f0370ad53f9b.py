def _setup_output_file(self, output_filename, args, write_header=True):
    try:
        output_file = open(output_filename, 'w')
    except IOError as e:
        sys.exit(e)
    if write_header:
        output_file.write(' '.join(map(util.escape_string_shell, self.
            _build_cmdline(args))) + '\n\n\n' + '-' * 80 + '\n\n\n')
        output_file.flush()
    return output_file