def write(self, output_filepath):
    with open(output_filepath, 'w') as out_file:
        out_file.write(self.__str__())