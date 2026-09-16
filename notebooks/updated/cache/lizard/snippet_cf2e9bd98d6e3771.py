def set_continuous(self, freq, amplitude, offset, output_state=True):
    commands = ['MODL 0', 'FREQ {0}'.format(freq)]
    if freq > 4050000000.0:
        commands.append('AMPH {0}'.format(amplitude))
        if offset > 0.0:
            print('HIGH FREQUENCY OUTPUT IS AC ONLY')
        if output_state is True:
            commands.append('ENBH 1')
        else:
            commands.append('ENBH 0')
    elif freq < 62500000.0:
        commands.extend(['AMPL {0}'.format(amplitude), 'OFSL {0}'.format(
            offset)])
        if output_state is True:
            commands.append('ENBL 1')
        else:
            commands.append('ENBL 0')
    command_string = '\n'.join(commands)
    print_string = '\n\t' + command_string.replace('\n', '\n\t')
    logging.info(print_string)
    self.instr.write(command_string)