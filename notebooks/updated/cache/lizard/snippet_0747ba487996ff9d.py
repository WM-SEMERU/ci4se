def main_color(self):
    if self.kind is None:
        return DEFAULT_COLOR
    elif self.kind == 'face':
        colors = self.face_colors
    elif self.kind == 'vertex':
        colors = self.vertex_colors
    else:
        raise ValueError('color kind incorrect!')
    unique, inverse = grouping.unique_rows(colors)
    mode_index = np.bincount(inverse).argmax()
    color = colors[unique[mode_index]]
    return color