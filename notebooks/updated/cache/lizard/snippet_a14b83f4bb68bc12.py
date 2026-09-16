def update_subtotals(self, current, sub_key):
    if not self.sub_counts.get(sub_key):
        self.sub_counts[sub_key] = {}
    for item in current:
        try:
            self.sub_counts[sub_key][item] += 1
        except KeyError:
            self.sub_counts[sub_key][item] = 1