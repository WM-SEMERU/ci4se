def on_segment(point_p, point_q, point_r):
    if point_q.x <= max(point_p.x, point_r.x) and point_q.x >= min(point_p.
        x, point_r.x) and point_q.y <= max(point_p.y, point_r.y
        ) and point_q.y >= min(point_p.y, point_r.y):
        return True
    return False