def save_to_filename(self, file_name, sep='\n'):
    fp = open(file_name, 'wb')
    n = self.save_to_file(fp, sep)
    fp.close()
    return n