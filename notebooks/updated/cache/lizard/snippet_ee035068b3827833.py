def create_clusters(provider, context, **kwargs):
    conn = get_session(provider.region).client('ecs')
    try:
        clusters = kwargs['clusters']
    except KeyError:
        logger.error('setup_clusters hook missing "clusters" argument')
        return False
    if isinstance(clusters, basestring):
        clusters = [clusters]
    cluster_info = {}
    for cluster in clusters:
        logger.debug('Creating ECS cluster: %s', cluster)
        r = conn.create_cluster(clusterName=cluster)
        cluster_info[r['cluster']['clusterName']] = r
    return {'clusters': cluster_info}