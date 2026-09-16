def AuthorizingClient(domain, auth, user_agent=None):
    http_transport = transport.HttpTransport(domain, build_headers(auth,
        user_agent))
    return client.Client(http_transport)