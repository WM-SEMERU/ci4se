def parse_list(self, entries):
    result_entries = SearchableList()
    for entry in entries:
        result_entries.append(self.instance.parse(self.requester, entry))
    return result_entries