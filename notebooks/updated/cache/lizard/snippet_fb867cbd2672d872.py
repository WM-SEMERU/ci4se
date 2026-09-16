def make_hex_texture(grid_size=2, resolution=1):
    grid_x, grid_y = np.meshgrid(np.arange(grid_size), np.arange(grid_size))
    ROOT_3_OVER_2 = np.sqrt(3) / 2
    ONE_HALF = 0.5
    grid_x = (grid_x * np.sqrt(3) + grid_y % 2 * ROOT_3_OVER_2).flatten()
    grid_y = grid_y.flatten() * 1.5
    grid_points = grid_x.shape[0]
    x_offsets = np.interp(np.arange(4 * resolution), np.arange(4) *
        resolution, [ROOT_3_OVER_2, 0.0, -ROOT_3_OVER_2, -ROOT_3_OVER_2])
    y_offsets = np.interp(np.arange(4 * resolution), np.arange(4) *
        resolution, [-ONE_HALF, -1.0, -ONE_HALF, ONE_HALF])
    tmx = 4 * resolution
    x_t = np.tile(grid_x, (tmx, 1)) + x_offsets.reshape((tmx, 1))
    y_t = np.tile(grid_y, (tmx, 1)) + y_offsets.reshape((tmx, 1))
    x_t = np.vstack([x_t, np.tile(np.nan, (1, grid_x.size))])
    y_t = np.vstack([y_t, np.tile(np.nan, (1, grid_y.size))])
    return fit_texture((x_t.flatten('F'), y_t.flatten('F')))