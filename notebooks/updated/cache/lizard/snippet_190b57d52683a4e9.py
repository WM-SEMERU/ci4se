def _get_ann_labels_data(self, order_ann, bins_ann):
    if self.yticks is None:
        return dict(x=[], y=[], text=[], angle=[])
    mapping = self._compute_tick_mapping('radius', order_ann, bins_ann)
    values = [(label, radius[0]) for label, radius in mapping.items()]
    labels, radius = zip(*values)
    radius = np.array(radius)
    y_coord = np.sin(np.deg2rad(self.yrotation)) * radius + self.max_radius
    x_coord = np.cos(np.deg2rad(self.yrotation)) * radius + self.max_radius
    return dict(x=x_coord, y=y_coord, text=labels, angle=[0] * len(labels))