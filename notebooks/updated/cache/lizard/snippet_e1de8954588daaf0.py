def hex16_to_u64be(data):
    return int(data[14:16] + data[12:14] + data[10:12] + data[8:10] + data[
        6:8] + data[4:6] + data[2:4] + data[0:2], 16)