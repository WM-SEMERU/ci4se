def handle(self, *file_paths, **options):
    import os
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print('File %s not found.' % file_path)
            continue
        f = open(file_path, 'r')
        data = f.readlines()
        f.close()
        self.parse_lines(data)