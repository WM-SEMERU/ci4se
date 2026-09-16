def createOptimizer(self, params, model):
    lr = params['learning_rate']
    print('Creating optimizer with learning rate=', lr)
    if params['optimizer'] == 'SGD':
        optimizer = optim.SGD(model.parameters(), lr=lr, momentum=params[
            'momentum'], weight_decay=params['weight_decay'])
    elif params['optimizer'] == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=lr)
    else:
        raise LookupError('Incorrect optimizer value')
    return optimizer