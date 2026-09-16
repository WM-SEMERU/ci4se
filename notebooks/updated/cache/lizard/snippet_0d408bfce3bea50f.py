def _check_completion_errors(self):
    if read_pattern(self.text, {'key':
        'Coordinates do not transform within specified threshold'},
        terminate_on_match=True).get('key') == [[]]:
        self.data['errors'] += ['failed_to_transform_coords']
    elif read_pattern(self.text, {'key':
        'The Q\\-Chem input file has failed to pass inspection'},
        terminate_on_match=True).get('key') == [[]]:
        self.data['errors'] += ['input_file_error']
    elif read_pattern(self.text, {'key': 'Error opening input stream'},
        terminate_on_match=True).get('key') == [[]]:
        self.data['errors'] += ['failed_to_read_input']
    elif read_pattern(self.text, {'key':
        'FileMan error: End of file reached prematurely'},
        terminate_on_match=True).get('key') == [[]]:
        self.data['errors'] += ['IO_error']
    elif read_pattern(self.text, {'key':
        'Could not find \\$molecule section in ParseQInput'},
        terminate_on_match=True).get('key') == [[]]:
        self.data['errors'] += ['read_molecule_error']
    elif read_pattern(self.text, {'key': 'Welcome to Q-Chem'},
        terminate_on_match=True).get('key') != [[]]:
        self.data['errors'] += ['never_called_qchem']
    else:
        self.data['errors'] += ['unknown_error']