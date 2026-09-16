def segment_to_vector(self, seg):
    ft_dict = {ft: val for val, ft in self.fts(seg)}
    return [ft_dict[name] for name in self.names]