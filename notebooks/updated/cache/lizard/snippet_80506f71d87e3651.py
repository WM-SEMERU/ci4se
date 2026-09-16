def createlogicalnetwork(create_processor=partial(default_processor,
    excluding=('id', 'physicalnetwork')), reorder_dict=default_iterate_dict):

    def walker(walk, write, timestamp, parameters_dict):
        for key, parameters in reorder_dict(parameters_dict):
            try:
                value = walk(key)
            except KeyError:
                pass
            else:
                id_ = parameters['id']
                lognet = create_new(LogicalNetwork, value, id_)
                logmap = LogicalNetworkMap.create_instance(id_)
                logmap.network = lognet.create_reference()
                try:
                    phynet = walk(PhysicalNetwork.default_key(parameters[
                        'physicalnetwork']))
                except KeyError:
                    pass
                else:
                    lognet.physicalnetwork = phynet.create_reference()
                    try:
                        phymap = walk(PhysicalNetworkMap._network.leftkey(
                            phynet))
                    except KeyError:
                        pass
                    else:
                        create_processor(lognet, logmap, phynet, phymap,
                            walk, write, parameters=parameters)
                        phymap.logicnetworks.dataset().add(lognet.
                            create_weakreference())
                        write(phymap.getkey(), phymap)
                        write(lognet.getkey(), lognet)
                        write(logmap.getkey(), logmap)
                try:
                    logicalnetworkset = walk(LogicalNetworkSet.default_key())
                except KeyError:
                    pass
                else:
                    logicalnetworkset.set.dataset().add(lognet.
                        create_weakreference())
                    write(logicalnetworkset.getkey(), logicalnetworkset)
    return walker