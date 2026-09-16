def _preprocess_data_for_tabular_explain(self, df, categories):
    df = df.copy()
    for col in list(df.columns):
        if col not in self._categorical_columns + self._numeric_columns:
            del df[col]
    for col_name, col_categories in zip(self._categorical_columns, categories):
        df[col_name] = df[col_name].apply(lambda x: col_categories.index(
            str(x)) if str(x) in col_categories else len(col_categories) - 1)
    for numeric_col in self._numeric_columns:
        df[numeric_col] = df[numeric_col].apply(lambda x: float(x))
    return df.as_matrix(self._categorical_columns + self._numeric_columns)