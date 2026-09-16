def vertical_is_complete(self, item):
    if item.location.block_type != 'vertical':
        raise ValueError('The passed in xblock is not a vertical type!')
    if not self.completion_tracking_enabled():
        return None
    child_locations = [child.location for child in item.get_children() if 
        child.location.block_type != 'discussion']
    completions = self.get_completions(child_locations)
    for child_location in child_locations:
        if completions[child_location] < 1.0:
            return False
    return True