def load_contents(self):
    with open(self.name + '.csv') as f:
        list_of_rows = f.readlines()
    list_of_rows = map(lambda x: x.strip(), map(lambda x: x.replace('"', ''
        ), list_of_rows))
    for row in list_of_rows:
        self.put_row(make_row(self.columns, row.split(',')))