def _parse(self, stream, context, path):
    num_players = context._._._.replay.num_players
    start = stream.tell()
    read_bytes = stream.read()
    marker_up14 = read_bytes.find(b'\x16\xc6\x00\x00\x00!')
    marker_up15 = read_bytes.find(b'\x16\xf0\x00\x00\x00!')
    marker = -1
    if marker_up14 > 0 and marker_up15 < 0:
        marker = marker_up14
    elif marker_up15 > 0 and marker_up14 < 0:
        marker = marker_up15
    if marker > 0:
        count = 0
        while struct.unpack('<H', read_bytes[marker - 2:marker])[0] != count:
            marker -= 1
            count += 1
        backtrack = 43 + num_players
    else:
        marker = read_bytes.find(b'\xf6(\x9c?')
        backtrack = 1817 * (num_players - 1) + 4 + 19
    end = start + marker - backtrack
    stream.seek(end)
    return end