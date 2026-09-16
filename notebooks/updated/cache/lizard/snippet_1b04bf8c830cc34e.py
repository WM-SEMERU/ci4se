def interp_box(x, y, z, box, values):
    val = 0
    norm = 0
    for i in range(8):
        distance = sqrt((x - box[i, 0]) ** 2 + (y - box[i, 1]) ** 2 + (z -
            box[i, 2]) ** 2)
        if distance == 0:
            val = values[i]
            norm = 1.0
            break
        w = 1.0 / distance
        val += w * values[i]
        norm += w
    return val / norm