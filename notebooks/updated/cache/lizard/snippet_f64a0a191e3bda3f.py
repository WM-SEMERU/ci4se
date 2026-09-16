def perform_command(self):
    if len(self.actual_arguments) < 1:
        return self.print_help()
    audio_file_path = self.actual_arguments[0]
    if not self.check_input_file(audio_file_path):
        return self.ERROR_EXIT_CODE
    try:
        prober = FFPROBEWrapper(rconf=self.rconf, logger=self.logger)
        dictionary = prober.read_properties(audio_file_path)
        for key in sorted(dictionary.keys()):
            self.print_generic('%s %s' % (key, dictionary[key]))
        return self.NO_ERROR_EXIT_CODE
    except FFPROBEPathError:
        self.print_error("Unable to call the ffprobe executable '%s'" %
            self.rconf[RuntimeConfiguration.FFPROBE_PATH])
        self.print_error('Make sure the path to ffprobe is correct')
    except (FFPROBEUnsupportedFormatError, FFPROBEParsingError):
        self.print_error("Cannot read properties of file '%s'" %
            audio_file_path)
        self.print_error(
            'Make sure the input file has a format supported by ffprobe')
    return self.ERROR_EXIT_CODE