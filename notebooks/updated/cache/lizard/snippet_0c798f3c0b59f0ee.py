def server_to_dict(server):
    soul = server.soul
    return {A.server.ID: server.href, A.server.PUBLIC_IPS: soul.get(
        'public_dns_names', []), A.server.PRIVATE_IPS: soul.get(
        'private_dns_names', [])}