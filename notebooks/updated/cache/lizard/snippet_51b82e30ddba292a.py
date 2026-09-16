def _HandleLegacy(self, args, token=None):
    hunt_urn = args.hunt_id.ToURN()
    hunt_obj = aff4.FACTORY.Open(hunt_urn, aff4_type=implementation.GRRHunt,
        token=token)
    clients_by_status = hunt_obj.GetClientsByStatus()
    hunt_clients = clients_by_status[args.client_status.name]
    total_count = len(hunt_clients)
    if args.count:
        hunt_clients = sorted(hunt_clients)[args.offset:args.offset + args.
            count]
    else:
        hunt_clients = sorted(hunt_clients)[args.offset:]
    flow_id = '%s:hunt' % hunt_urn.Basename()
    results = [ApiHuntClient(client_id=c.Basename(), flow_id=flow_id) for c in
        hunt_clients]
    return ApiListHuntClientsResult(items=results, total_count=total_count)