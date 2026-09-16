def get_column(self, name):
    import ibis.expr.operations as ops
    ref = ops.TableColumn(name, self)
    return ref.to_expr()