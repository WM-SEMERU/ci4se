def get_action_side_effects(self):
    result = SCons.Util.UniqueList([])
    for target in self.get_action_targets():
        result.extend(target.side_effects)
    return result