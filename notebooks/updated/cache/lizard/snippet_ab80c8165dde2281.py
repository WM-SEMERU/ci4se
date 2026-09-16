def check_abbreviation_unique(self, abbreviation, newFilterPattern, targetItem
    ):
    for item in self.allFolders:
        if model.TriggerMode.ABBREVIATION in item.modes:
            if abbreviation in item.abbreviations and item.filter_matches(
                newFilterPattern):
                return item is targetItem, item
    for item in self.allItems:
        if model.TriggerMode.ABBREVIATION in item.modes:
            if abbreviation in item.abbreviations and item.filter_matches(
                newFilterPattern):
                return item is targetItem, item
    return True, None