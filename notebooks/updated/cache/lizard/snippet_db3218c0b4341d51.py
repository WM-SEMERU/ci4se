def filter_components(self, pattern, category=None):
    filtered_components = []
    for component, profile in self:
        if category:
            if profile.category != category:
                continue
        if re.search(pattern, component):
            filtered_components.append(component)
    return filtered_components