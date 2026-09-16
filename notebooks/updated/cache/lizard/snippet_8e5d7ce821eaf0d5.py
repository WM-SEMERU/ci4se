def id_range(self):
    if len(self._anchor_points) == 0:
        return 0, 0
    return self._anchor_points[0].reading_id, self._anchor_points[-1
        ].reading_id