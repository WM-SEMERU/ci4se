def _input_as_multiline_string(self, data):
    self._input_filename = self.getTmpFilename(self.WorkingDir, suffix='.fasta'
        )
    with open(self._input_filename, 'w') as f:
        f.write(data)
    return self._input_filename