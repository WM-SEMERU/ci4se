def _reset_model(self, table, model):
    old_sel_model = table.selectionModel()
    table.setModel(model)
    if old_sel_model:
        del old_sel_model