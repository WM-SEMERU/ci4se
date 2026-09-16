def map_equal_contributions(contributors):
    equal_contribution_map = {}
    equal_contribution_keys = []
    for contributor in contributors:
        if contributor.get('references'
            ) and 'equal-contrib' in contributor.get('references'):
            for key in contributor['references']['equal-contrib']:
                if key not in equal_contribution_keys:
                    equal_contribution_keys.append(key)
    equal_contribution_keys = sorted(equal_contribution_keys)
    for i, equal_contribution_key in enumerate(equal_contribution_keys):
        equal_contribution_map[equal_contribution_key] = i + 1
    return equal_contribution_map