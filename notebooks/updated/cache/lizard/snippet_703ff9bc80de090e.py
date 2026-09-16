def _pack_people(people):
    res = bytearray()
    bits = bytearray([1])
    for person in people:
        bits.extend(person.to_bits())
    aByte = 0
    for i, bit in enumerate(bits[::-1]):
        mod = i % 8
        aByte |= bit << mod
        if mod == 7 or i == len(bits) - 1:
            res.append(aByte)
            aByte = 0
    return struct.pack(APPUpdateMessage.fmt.format(len(res)), *res[::-1])