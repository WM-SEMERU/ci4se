def rpc_call(payload):
    corr_id = RPC_CLIENT.send_request(payload)
    while RPC_CLIENT.queue[corr_id] is None:
        sleep(0.1)
    return RPC_CLIENT.queue[corr_id]