def get_F_y(fname='binzegger_connectivity_table.json', y=['p23']):
    f = open(fname, 'r')
    data = json.load(f)
    f.close()
    occurr = []
    for cell_type in y:
        occurr += [data['data'][cell_type]['occurrence']]
    return list(np.array(occurr) / np.sum(occurr))