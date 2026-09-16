def create_connector_c_pool(name, server=None, **kwargs):
    defaults = {'connectionDefinitionName': 'javax.jms.ConnectionFactory',
        'resourceAdapterName': 'jmsra', 'associateWithThread': False,
        'connectionCreationRetryAttempts': 0,
        'connectionCreationRetryIntervalInSeconds': 0,
        'connectionLeakReclaim': False, 'connectionLeakTimeoutInSeconds': 0,
        'description': '', 'failAllConnections': False, 'id': name,
        'idleTimeoutInSeconds': 300, 'isConnectionValidationRequired':
        False, 'lazyConnectionAssociation': False,
        'lazyConnectionEnlistment': False, 'matchConnections': True,
        'maxConnectionUsageCount': 0, 'maxPoolSize': 32,
        'maxWaitTimeInMillis': 60000, 'ping': False, 'poolResizeQuantity': 
        2, 'pooling': True, 'steadyPoolSize': 8, 'target': 'server',
        'transactionSupport': '', 'validateAtmostOncePeriodInSeconds': 0}
    data = defaults
    data.update(kwargs)
    if data['transactionSupport'] and data['transactionSupport'] not in (
        'XATransaction', 'LocalTransaction', 'NoTransaction'):
        raise CommandExecutionError('Invalid transaction support')
    return _create_element(name, 'resources/connector-connection-pool',
        data, server)