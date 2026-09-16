def sum(self):
    return LazyOpResult(grizzly_impl.aggr(self.expr, '+', 0, self.weld_type
        ), self.weld_type, 0)