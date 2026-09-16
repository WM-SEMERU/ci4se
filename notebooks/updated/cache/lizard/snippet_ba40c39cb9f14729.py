def get_grid_point_from_address(grid_address, mesh):
    _set_no_error()
    return spg.grid_point_from_address(np.array(grid_address, dtype='intc'),
        np.array(mesh, dtype='intc'))