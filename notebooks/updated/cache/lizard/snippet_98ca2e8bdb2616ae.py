def _unstack(self, unstacker_func, new_columns, n_rows, fill_value):
    unstacker = unstacker_func(self.values.T)
    new_items = unstacker.get_new_columns()
    new_placement = new_columns.get_indexer(new_items)
    new_values, mask = unstacker.get_new_values()
    mask = mask.any(0)
    new_values = new_values.T[mask]
    new_placement = new_placement[mask]
    blocks = [make_block(new_values, placement=new_placement)]
    return blocks, mask