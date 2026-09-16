def reverse_segment(path, n1, n2):
    q = path.copy()
    if n2 > n1:
        q[n1:n2 + 1] = path[n1:n2 + 1][::-1]
        return q
    else:
        seg = np.hstack((path[n1:], path[:n2 + 1]))[::-1]
        brk = len(q) - n1
        q[n1:] = seg[:brk]
        q[:n2 + 1] = seg[brk:]
        return q