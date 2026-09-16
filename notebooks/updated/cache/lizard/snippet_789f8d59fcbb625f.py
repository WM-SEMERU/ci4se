def set_column_si_format(tree_column, model_column_index, cell_renderer=
    None, digits=2):

    def set_property(column, cell_renderer, list_store, iter, store_i):
        cell_renderer.set_property('text', si_format(list_store[iter][
            store_i], digits))
    if cell_renderer is None:
        cells = tree_column.get_cells()
    else:
        cells = [cell_renderer]
    for cell_renderer_i in cells:
        tree_column.set_cell_data_func(cell_renderer_i, set_property,
            model_column_index)