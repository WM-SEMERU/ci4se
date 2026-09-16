def find_all(self, string, callback):
    for index, output in self.iter(string):
        callback(index, output)