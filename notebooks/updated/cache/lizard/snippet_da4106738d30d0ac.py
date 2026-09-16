def import_oracle(self):
    return ImportOracle(go_dist=self.go_dist, workunit_factory=self.context
        .new_workunit)