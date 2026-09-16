def af_for_address(text):
    try:
        junk = dns.ipv4.inet_aton(text)
        return AF_INET
    except Exception:
        try:
            junk = dns.ipv6.inet_aton(text)
            return AF_INET6
        except Exception:
            raise ValueError