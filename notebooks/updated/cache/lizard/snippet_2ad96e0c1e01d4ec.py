def create_table_from_object(self, obj):
    get_type = lambda item: str(type(item)).split("'")[1]
    if not os.path.exists(os.path.join(self.db_path, obj._TABLE)):
        with gzip.open(os.path.join(self.db_path, obj._TABLE), 'wb'
            ) as table_file:
            csv.writer(table_file).writerow(['{col}:{type}'.format(col=elm[
                0], type=get_type(elm[1])) for elm in tuple(obj.__dict__.
                items())])
        self._tables[obj._TABLE] = self._load_table(obj._TABLE)