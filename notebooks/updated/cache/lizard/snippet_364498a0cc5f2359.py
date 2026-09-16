def parse_file_to_dict(self, fname):
    print('TODO - parse_file_to_dict' + fname)
    for m in self.maps:
        if m.tpe == 'file':
            if m.key[0:3] == 'col':
                print('reading column..')