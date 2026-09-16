def grid_situate(self, current_idx, layout_type, subgrid_width):
    if layout_type == 'Single':
        start, inds = current_idx + 1, [current_idx]
    elif layout_type == 'Dual':
        start, inds = current_idx + 2, [current_idx, current_idx + 1]
    bottom_idx = current_idx + subgrid_width
    if layout_type == 'Embedded Dual':
        bottom = (current_idx + 1) % subgrid_width == 0
        grid_idx = (bottom_idx if bottom else current_idx) + 1
        start, inds = grid_idx, [current_idx, bottom_idx]
    elif layout_type == 'Triple':
        bottom = (current_idx + 2) % subgrid_width == 0
        grid_idx = (bottom_idx if bottom else current_idx) + 2
        start, inds = grid_idx, [current_idx, current_idx + 1, bottom_idx, 
            bottom_idx + 1]
    return start, inds