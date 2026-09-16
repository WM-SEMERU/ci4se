def annotate(self, framedata):
    for artist in self.annotation_artists:
        artist.remove()
    self.annotation_artists = []
    for annotation in self.annotations:
        if annotation[2] > framedata:
            return
        if annotation[2] == framedata:
            pos = annotation[0:2]
            shape = self.annotations_default['shape']
            color = self.annotations_default['color']
            size = self.annotations_default['size']
            line = self.annotations_default['line']
            if len(annotation) > 3:
                shape = annotation[3].get('shape', shape)
                color = annotation[3].get('color', color)
                size = annotation[3].get('size', size)
                line = annotation[3].get('line', line)
            if shape == 'CIRC' and hasattr(size, '__len__'):
                size = 30
            if not hasattr(color, '__len__'):
                color = (color,) * 3
            if shape == 'RECT':
                patch = patches.Rectangle((pos[0] - size[0] // 2, pos[1] - 
                    size[1] // 2), size[0], size[1], fill=False, lw=line,
                    fc='none', ec=color)
            elif shape == 'CIRC':
                patch = patches.CirclePolygon(pos, radius=size, fc='none',
                    ec=color, lw=line)
            self.annotation_artists.append(patch)
            self.axes_processed.add_artist(self.annotation_artists[-1])