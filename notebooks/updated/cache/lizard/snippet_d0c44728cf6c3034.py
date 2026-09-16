def get_index_of_column(cls, column, file_path):
    columns = cls.get_column_names_from_file(file_path)
    if column in columns:
        return columns.index(column)