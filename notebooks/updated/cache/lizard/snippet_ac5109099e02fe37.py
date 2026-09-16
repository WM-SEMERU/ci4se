def save_state(self, fname):
    log.info('Saving state to %s', fname)
    data = {'ksize': self.ksize, 'alpha': self.alpha, 'id': self.node.id,
        'neighbors': self.bootstrappable_neighbors()}
    if not data['neighbors']:
        log.warning('No known neighbors, so not writing to cache.')
        return
    with open(fname, 'wb') as file:
        pickle.dump(data, file)