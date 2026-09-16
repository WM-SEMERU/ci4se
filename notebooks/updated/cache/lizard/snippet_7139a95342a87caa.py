def find_best_matching_node(self, new, old_nodes):
    name = new.__class__.__name__
    matches = [c for c in old_nodes if name == c.__class__.__name__]
    if self.debug:
        print('Found matches for {}: {} '.format(new, matches))
    return matches[0] if matches else None