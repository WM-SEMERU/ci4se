def join_ops(ops1, ops2):
    i = len(ops1) - 1
    j = 0
    while i >= 0 and j < len(ops2):
        if ops1[i] == ops2[j]:
            i -= 1
            j += 1
        else:
            break
    return ops1[:i + 1] + ops2[j:]