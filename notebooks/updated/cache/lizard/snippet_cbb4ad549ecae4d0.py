def add_node(cls, cluster_id_label, parameters=None):
    conn = Qubole.agent(version=Cluster.api_version)
    parameters = {} if not parameters else parameters
    return conn.post(cls.element_path(cluster_id_label) + '/nodes', data={
        'parameters': parameters})