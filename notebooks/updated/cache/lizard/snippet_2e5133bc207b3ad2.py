def filter_by_keyword(self, keyword):
    filtered_days = []
    for des_day in self.design_days:
        if keyword in des_day.name:
            filtered_days.append(des_day)
    return filtered_days