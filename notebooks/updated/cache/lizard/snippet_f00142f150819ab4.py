def load_data(filename):
    data = pandas.read_csv(filename, header=None, delimiter='\t', skiprows=9)
    return data.as_matrix()