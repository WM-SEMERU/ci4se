def existing_sub_paths(self, sub_paths):
    paths_to_subs = [(self / _) for _ in sub_paths]
    return [_ for _ in paths_to_subs if _.exists()]