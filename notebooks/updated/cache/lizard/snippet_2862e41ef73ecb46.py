def load_network_from_file(filename):
    import cPickle
    network = NeuralNet({'n_inputs': 1, 'layers': [[0, None]]})
    with open(filename, 'rb') as file:
        store_dict = cPickle.load(file)
        network.n_inputs = store_dict['n_inputs']
        network.n_weights = store_dict['n_weights']
        network.layers = store_dict['layers']
        network.weights = store_dict['weights']
    return network