def available_resources(self):
    available_resources_by_id = {}
    subscribe_clients = [redis_client.pubsub(ignore_subscribe_messages=True
        ) for redis_client in self.redis_clients]
    for subscribe_client in subscribe_clients:
        subscribe_client.subscribe(ray.gcs_utils.XRAY_HEARTBEAT_CHANNEL)
    client_ids = self._live_client_ids()
    while set(available_resources_by_id.keys()) != client_ids:
        for subscribe_client in subscribe_clients:
            raw_message = subscribe_client.get_message()
            if raw_message is None or raw_message['channel'
                ] != ray.gcs_utils.XRAY_HEARTBEAT_CHANNEL:
                continue
            data = raw_message['data']
            gcs_entries = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(
                data, 0)
            heartbeat_data = gcs_entries.Entries(0)
            message = (ray.gcs_utils.HeartbeatTableData.
                GetRootAsHeartbeatTableData(heartbeat_data, 0))
            num_resources = message.ResourcesAvailableLabelLength()
            dynamic_resources = {}
            for i in range(num_resources):
                resource_id = decode(message.ResourcesAvailableLabel(i))
                dynamic_resources[resource_id
                    ] = message.ResourcesAvailableCapacity(i)
            client_id = ray.utils.binary_to_hex(message.ClientId())
            available_resources_by_id[client_id] = dynamic_resources
        client_ids = self._live_client_ids()
        for client_id in available_resources_by_id.keys():
            if client_id not in client_ids:
                del available_resources_by_id[client_id]
    total_available_resources = defaultdict(int)
    for available_resources in available_resources_by_id.values():
        for resource_id, num_available in available_resources.items():
            total_available_resources[resource_id] += num_available
    for subscribe_client in subscribe_clients:
        subscribe_client.close()
    return dict(total_available_resources)