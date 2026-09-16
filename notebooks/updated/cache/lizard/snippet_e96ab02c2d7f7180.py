def delta_decode(in_array):
    if len(in_array) == 0:
        return []
    this_ans = in_array[0]
    out_array = [this_ans]
    for i in range(1, len(in_array)):
        this_ans += in_array[i]
        out_array.append(this_ans)
    return out_array