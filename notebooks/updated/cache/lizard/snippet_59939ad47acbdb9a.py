def write_file(self, filename):
    writer = self.__str__()[:-1].decode('utf-8')
    with open(filename, 'w') as fout:
        fout.write(writer)