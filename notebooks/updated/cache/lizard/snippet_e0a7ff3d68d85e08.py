def unique_id(length=12, increment=0):
    head = np.array((increment + time.time() * 10) % 2 ** 16, dtype=np.uint16
        ).tostring()
    random = np.random.random(int(np.ceil(length / 5))).tostring()
    unique = base64.b64encode(head + random, b'  ').decode('utf-8')
    unique = unique.replace(' ', '')[:length]
    return unique