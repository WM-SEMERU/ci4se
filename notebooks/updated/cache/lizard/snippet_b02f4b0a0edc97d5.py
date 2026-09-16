def find_all(self):
    with open(self._csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=self._delimiter)
        return [self._movie_model(*row) for row in csv_reader]