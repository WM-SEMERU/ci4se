def get_all_network_owners(network_ids=None, **kwargs):
    networkowner_qry = db.DBSession.query(NetworkOwner)
    if network_ids is not None:
        networkowner_qry = networkowner_qry.filter(NetworkOwner.network_id.
            in_(network_ids))
    network_owners_i = networkowner_qry.all()
    return [JSONObject(network_owner_i) for network_owner_i in network_owners_i
        ]