def create(self):
    if self.bt_table.exists():
        utils.dbg('Table already exists')
        return
    max_versions_rule = bigtable_column_family.MaxVersionsGCRule(1)
    self.bt_table.create(column_families={METADATA: max_versions_rule,
        TFEXAMPLE: max_versions_rule})