def site_coordination_numbers(self):
    coordination_numbers = {}
    for l in self.site_labels:
        coordination_numbers[l] = set([len(site.neighbours) for site in
            self.sites if site.label is l])
    return coordination_numbers