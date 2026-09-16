def format_addresses(addrs):
    return ', '.join(formataddr(item) if isinstance(item, tuple) else item for
        item in addrs)