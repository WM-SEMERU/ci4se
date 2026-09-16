def map_data(self):
    with open(self.src_file, 'r') as f:
        for line in f:
            cols = line.split(',')
            print(cols)