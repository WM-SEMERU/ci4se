def is_early_compact_l2a(self):
    return (self.data_source is DataSource.SENTINEL2_L2A and self.safe_type is
        EsaSafeType.COMPACT_TYPE and self.baseline <= '02.06')