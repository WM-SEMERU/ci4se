def _get_table_cells(table):
    sent_map = defaultdict(list)
    for sent in table.sentences:
        if sent.is_tabular():
            sent_map[sent.cell].append(sent)
    return sent_map