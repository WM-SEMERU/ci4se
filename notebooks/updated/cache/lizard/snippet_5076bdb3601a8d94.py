def load_data(self, table_name, obj, **kwargs):
    self.dictionary[table_name] = pd.DataFrame(obj)