def filter(self, predicates):
    tys = []
    for col_name, raw_column in self.raw_columns.items():
        dtype = str(raw_column.dtype)
        if dtype == 'object' or dtype == '|S64':
            weld_type = WeldVec(WeldChar())
        else:
            weld_type = grizzly_impl.numpy_to_weld_type_mapping[dtype]
        tys.append(weld_type)
    if len(tys) == 1:
        weld_type = tys[0]
    else:
        weld_type = WeldStruct(tys)
    if isinstance(predicates, SeriesWeld):
        predicates = predicates.expr
    return DataFrameWeldExpr(grizzly_impl.filter(grizzly_impl.zip_columns(
        self.raw_columns.values()), predicates), self.raw_columns.keys(),
        weld_type)