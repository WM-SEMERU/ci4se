def _add_instruction(self, instruction, value):
    if (instruction == 'LABEL' or instruction == 'ENV') and len(value) == 2:
        new_line = instruction + ' ' + '='.join(map(quote, value)) + '\n'
    else:
        new_line = '{0} {1}\n'.format(instruction, value)
    if new_line:
        lines = self.lines
        if not lines[len(lines) - 1].endswith('\n'):
            new_line = '\n' + new_line
        lines += new_line
        self.lines = lines