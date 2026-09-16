def filter_by_program(self, prg, opFile):
    log_1 = open(self.process_file, 'r')
    log_2 = open(self.command_file, 'r')
    log_3 = open(self.result_file, 'r')
    log_4 = open(self.source_file, 'r')
    with open(opFile, 'a') as f:
        for line in log_1:
            if prg in line:
                f.write('PROCESS, ' + line)
        for line in log_2:
            if prg in line:
                f.write('COMMAND, ' + line)
        for line in log_3:
            if prg in line:
                f.write('RESULT, ' + line)
        for line in log_4:
            if prg in line:
                f.write('SOURCE, ' + line)
    log_1.close()
    log_2.close()
    log_3.close()
    log_4.close()