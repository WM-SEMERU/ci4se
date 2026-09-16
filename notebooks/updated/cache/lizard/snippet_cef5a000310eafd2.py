def mapper(self):
    if not self.__mapper:
        for model in table_conf.models_to_map:
            domain = model.table_suffix
            tab_conf = table_conf.tables[model]
            file_path = os.path.join(self.pyctd_data_dir, tab_conf['file_name']
                )
            col_name_in_file, col_name_in_db = tab_conf['domain_id_column']
            column_index = self.get_index_of_column(col_name_in_file, file_path
                )
            df = pd.read_table(file_path, names=[col_name_in_db], header=
                None, usecols=[column_index], comment='#', index_col=False,
                dtype=self.get_dtypes(model))
            if domain == 'chemical':
                df[col_name_in_db] = df[col_name_in_db].str.replace('MESH:', ''
                    ).str.strip()
            df[domain + '__id'] = df.index + 1
            self.__mapper[domain] = df
    return self.__mapper