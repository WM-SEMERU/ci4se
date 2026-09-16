def reorder_release_entries(releases):
    order = {'feature': 0, 'bug': 1, 'support': 2}
    for release in releases:
        entries = release['entries'][:]
        release['entries'] = sorted(entries, key=lambda x: order[x.type])