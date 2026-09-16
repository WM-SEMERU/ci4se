def ipv4_generate_random(total=100):
    count = 0
    yielded = set()
    while count < total:
        address = str(IPv4Address(random.randint(0, 2 ** 32 - 1)))
        if not ipv4_is_defined(address)[0] and address not in yielded:
            count += 1
            yielded.add(address)
            yield address