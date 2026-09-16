def case(self, case_id=None):
    if case_id:
        for case in self.case_objs:
            if case.case_id == case_id:
                return case
    elif self.cases:
        return list(self.case_objs)[0]
    return Case(case_id='unknown')