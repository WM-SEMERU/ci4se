def papermill_process(self, nb_man, resources):
    nb = nb_man.nb
    for index, cell in enumerate(nb.cells):
        try:
            nb_man.cell_start(cell, index)
            if not cell.source:
                continue
            nb.cells[index], resources = self.preprocess_cell(cell,
                resources, index)
        except CellExecutionError as ex:
            nb_man.cell_exception(nb.cells[index], cell_index=index,
                exception=ex)
            break
        finally:
            nb_man.cell_complete(nb.cells[index], cell_index=index)
    return nb, resources