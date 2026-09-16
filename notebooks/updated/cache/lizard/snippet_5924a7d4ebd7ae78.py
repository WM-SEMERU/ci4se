def identify_denonavr_receivers():
    devices = send_ssdp_broadcast()
    receivers = []
    for device in devices:
        try:
            receiver = evaluate_scpd_xml(device['URL'])
        except ConnectionError:
            continue
        if receiver:
            receivers.append(receiver)
    return receivers