def calculate_view_box(layers, aspect_ratio, margin=DEFAULT_VIEW_BOX_MARGIN):
    min_x = min(np.nanmin(x) for x, y in layers)
    max_x = max(np.nanmax(x) for x, y in layers)
    min_y = min(np.nanmin(y) for x, y in layers)
    max_y = max(np.nanmax(y) for x, y in layers)
    height = max_y - min_y
    width = max_x - min_x
    if height > width * aspect_ratio:
        adj_height = height * (1.0 + margin)
        adj_width = adj_height / aspect_ratio
    else:
        adj_width = width * (1.0 + margin)
        adj_height = adj_width * aspect_ratio
    width_buffer = (adj_width - width) / 2.0
    height_buffer = (adj_height - height) / 2.0
    return min_x - width_buffer, min_y - height_buffer, adj_width, adj_height