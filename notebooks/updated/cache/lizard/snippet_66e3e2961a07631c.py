def load_config(self, filename=None, replace=True, verbose=True):
    loaded_existing = True
    if filename is None:
        filename = standard_config_filename()
        if exists(filename):
            if verbose:
                print("Using existing configuration '{}' as base".format(
                    filename))
        else:
            filename = self.defconfig_filename
            if filename is None:
                if verbose:
                    print('Using default symbol values as base')
                return False
            if verbose:
                print("Using default configuration found in '{}' as base".
                    format(filename))
            loaded_existing = False
    self._warn_for_no_prompt = False
    try:
        self._load_config(filename, replace)
    except UnicodeDecodeError as e:
        _decoding_error(e, filename)
    finally:
        self._warn_for_no_prompt = True
    return loaded_existing