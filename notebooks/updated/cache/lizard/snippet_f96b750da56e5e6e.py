def get_vpc_overview(con, vpc_id, region_name):
    logging.debug("Retrieving information for VPC '%s'" % vpc_id)
    d = {}
    d['zones'] = con.get_all_zones()
    all_vpcs = con.get_all_vpcs()
    if not all_vpcs:
        raise VpcRouteSetError('Cannot find any VPCs.')
    if not vpc_id:
        vpc = all_vpcs[0]
        vpc_id = vpc.id
    else:
        vpc = None
        for v in all_vpcs:
            if v.id == vpc_id:
                vpc = v
                break
        if not vpc:
            raise VpcRouteSetError(
                "Cannot find specified VPC '%s' in region '%s'." % (vpc_id,
                region_name))
    d['vpc'] = vpc
    vpc_filter = {'vpc-id': vpc_id}
    d['subnets'] = con.get_all_subnets(filters=vpc_filter)
    d['route_tables'] = con.get_all_route_tables(filters=vpc_filter)
    d['rt_subnet_lookup'] = {}
    for rt in d['route_tables']:
        for assoc in rt.associations:
            if hasattr(assoc, 'subnet_id'):
                subnet_id = assoc.subnet_id
                if subnet_id:
                    d['rt_subnet_lookup'].setdefault(rt.id, []).append(
                        subnet_id)
    reservations = con.get_all_reservations(filters=vpc_filter)
    d['instances'] = []
    for r in reservations:
        d['instances'].extend(r.instances)
    _make_ip_subnet_lookup(d)
    d['instance_by_id'] = {}
    for i in d['instances']:
        d['instance_by_id'][i.id] = i
    return d