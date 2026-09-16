def _prepare_client(client_or_address):
    if client_or_address is None or str(client_or_address).lower() == 'local':
        local_cluster = LocalCluster(diagnostics_port=None)
        client = Client(local_cluster)

        def close_client_and_local_cluster(verbose=False):
            if verbose:
                print('shutting down client and local cluster')
            client.close()
            local_cluster.close()
        return client, close_client_and_local_cluster
    elif isinstance(client_or_address, str) and client_or_address.lower(
        ) != 'local':
        client = Client(client_or_address)

        def close_client(verbose=False):
            if verbose:
                print('shutting down client')
            client.close()
        return client, close_client
    elif isinstance(client_or_address, Client):

        def close_dummy(verbose=False):
            if verbose:
                print('not shutting down client, client was created externally'
                    )
            return None
        return client_or_address, close_dummy
    else:
        raise ValueError('Invalid client specified {}'.format(str(
            client_or_address)))