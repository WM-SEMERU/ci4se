def set_column_format(tree_column, model_column_index, format_str,
    cell_renderer=None):

    def set_property(column, cell_renderer, list_store, iter, store_i):
        value = list_store[iter][store_i]
        cell_renderer.set_property('text', format_str.format(value=value))
    if cell_renderer is None:
        cells = tree_column.get_cells()
    else:
        cells = [cell_renderer]
    for cell_renderer_i in cells:
        tree_column.set_cell_data_func(cell_renderer_i, set_property,
            model_column_index)