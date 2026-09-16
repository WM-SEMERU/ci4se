def magic_memory(self, line):
    message = ''
    for address in [i.strip() for i in line.replace(',', '').split()]:
        if '-' in address:
            m1, m2 = address.split('-')
            n1 = re.search(self.interpreter.IMMEDIATE_NUMBER, m1).groups()[0]
            n2 = re.search(self.interpreter.IMMEDIATE_NUMBER, m2).groups()[0]
            n1 = self.interpreter.convert_to_integer(n1)
            n2 = self.interpreter.convert_to_integer(n2)
            for i in range(n1, n2 + 1):
                val = self.interpreter.memory[i]
                val = self.convert_representation(val)
                message += '{}: {}\n'.format(str(i), val)
        else:
            val = self.interpreter.memory[self.interpreter.
                convert_to_integer(address)]
            val = self.convert_representation(val)
            message += '{}: {}\n'.format(address, val)
    stream_content = {'name': 'stdout', 'text': message}
    self.send_response(self.iopub_socket, 'stream', stream_content)