def StopHuntIfCPUOrNetworkLimitsExceeded(hunt_id):
    hunt_obj = data_store.REL_DB.ReadHuntObject(hunt_id)
    if hunt_obj.hunt_state == rdf_hunt_objects.Hunt.HuntState.STOPPED:
        return hunt_obj
    hunt_counters = data_store.REL_DB.ReadHuntCounters(hunt_id)
    if (hunt_obj.total_network_bytes_limit and hunt_counters.
        total_network_bytes_sent > hunt_obj.total_network_bytes_limit):
        reason = (
            'Hunt %s reached the total network bytes sent limit of %d and was stopped.'
             % (hunt_obj.hunt_id, hunt_obj.total_network_bytes_limit))
        return StopHunt(hunt_obj.hunt_id, reason=reason)
    if hunt_counters.num_clients < MIN_CLIENTS_FOR_AVERAGE_THRESHOLDS:
        return hunt_obj
    if hunt_obj.avg_results_per_client_limit:
        avg_results_per_client = (hunt_counters.num_results / hunt_counters
            .num_clients)
        if avg_results_per_client > hunt_obj.avg_results_per_client_limit:
            reason = (
                'Hunt %s reached the average results per client limit of %d and was stopped.'
                 % (hunt_obj.hunt_id, hunt_obj.avg_results_per_client_limit))
            return StopHunt(hunt_obj.hunt_id, reason=reason)
    if hunt_obj.avg_cpu_seconds_per_client_limit:
        avg_cpu_seconds_per_client = (hunt_counters.total_cpu_seconds /
            hunt_counters.num_clients)
        if (avg_cpu_seconds_per_client > hunt_obj.
            avg_cpu_seconds_per_client_limit):
            reason = (
                'Hunt %s reached the average CPU seconds per client limit of %d and was stopped.'
                 % (hunt_obj.hunt_id, hunt_obj.
                avg_cpu_seconds_per_client_limit))
            return StopHunt(hunt_obj.hunt_id, reason=reason)
    if hunt_obj.avg_network_bytes_per_client_limit:
        avg_network_bytes_per_client = (hunt_counters.
            total_network_bytes_sent / hunt_counters.num_clients)
        if (avg_network_bytes_per_client > hunt_obj.
            avg_network_bytes_per_client_limit):
            reason = (
                'Hunt %s reached the average network bytes per client limit of %d and was stopped.'
                 % (hunt_obj.hunt_id, hunt_obj.
                avg_network_bytes_per_client_limit))
            return StopHunt(hunt_obj.hunt_id, reason=reason)
    return hunt_obj