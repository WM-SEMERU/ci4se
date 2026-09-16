def bbox(self):
    bbox = self._df[['id', 'x1', 'y1', 'x2', 'y2']].copy()
    if self.bbox_with_size:
        bbox['y2'] -= bbox['y1']
        bbox['x2'] -= bbox['x1']
    return to_array_list(bbox)