def expand_variables(self):
    self.environment['INPUTS'] = ' '.join(self.inputs)
    self.environment['OUTPUTS'] = ' '.join(self.outputs)
    for n, input_file in enumerate(self.inputs):
        self.environment['INPUT{}'.format(n + 1)] = input_file
    for n, output_file in enumerate(self.outputs):
        self.environment['OUTPUT{}'.format(n + 1)] = output_file
    for n, line in enumerate(self.code):
        match = self.__variable_pattern.findall(line)
        if len(match) > 0:
            for item in match:
                value = self.environment.get(item)
                if value is not None:
                    self.code[n] = self.code[n].replace('$[' + item + ']',
                        value)