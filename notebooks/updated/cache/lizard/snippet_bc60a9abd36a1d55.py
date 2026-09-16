def get_autoconfig_client(client_cache=_AUTOCONFIG_CLIENT):
    try:
        return client_cache.client
    except AttributeError:
        configured_client = hdfs_config.get_configured_hdfs_client()
        if configured_client == 'webhdfs':
            client_cache.client = hdfs_webhdfs_client.WebHdfsClient()
        elif configured_client == 'snakebite':
            client_cache.client = hdfs_snakebite_client.SnakebiteHdfsClient()
        elif configured_client == 'snakebite_with_hadoopcli_fallback':
            client_cache.client = luigi.contrib.target.CascadingClient([
                hdfs_snakebite_client.SnakebiteHdfsClient(),
                hdfs_hadoopcli_clients.create_hadoopcli_client()])
        elif configured_client == 'hadoopcli':
            client_cache.client = (hdfs_hadoopcli_clients.
                create_hadoopcli_client())
        else:
            raise Exception('Unknown hdfs client ' + configured_client)
        return client_cache.client