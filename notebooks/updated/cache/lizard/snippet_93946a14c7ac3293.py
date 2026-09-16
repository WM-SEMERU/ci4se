def lower(self):
    vectype = self.weld_type
    if isinstance(vectype, WeldVec):
        elem_type = vectype.elemType
        if isinstance(elem_type, WeldChar):
            return SeriesWeld(grizzly_impl.to_lower(self.expr, elem_type),
                self.weld_type, self.df, self.column_name)
    raise Exception('Cannot call to_lower on non string type')