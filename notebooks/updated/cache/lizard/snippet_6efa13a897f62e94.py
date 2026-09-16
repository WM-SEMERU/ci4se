def insert_data(self, node, data, start, end):
    for item in data:
        self.recursive_insert(node, [item[0], item[1]], item[-1], start, end)