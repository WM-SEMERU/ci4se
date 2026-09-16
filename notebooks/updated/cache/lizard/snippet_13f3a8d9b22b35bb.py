def GetLaunchedFlows(self, flow_type='outstanding'):
    result = None
    all_clients = set(self.ListAllClients())
    finished_clients = set(self.ListFinishedClients())
    outstanding_clients = all_clients - finished_clients
    if flow_type == 'all':
        result = all_clients
    elif flow_type == 'finished':
        result = finished_clients
    elif flow_type == 'outstanding':
        result = outstanding_clients
    flows = aff4.FACTORY.MultiListChildren([self.urn.Add(x.Basename()) for
        x in result])
    return [x[0] for _, x in flows]