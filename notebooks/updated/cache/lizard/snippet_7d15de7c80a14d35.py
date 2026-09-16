def _get_group_attributes(self, index):
    g_case = None, None, -1
    for group in self.group_slots:
        if group[0] == index:
            g_case = group[1]
            break
    return g_case