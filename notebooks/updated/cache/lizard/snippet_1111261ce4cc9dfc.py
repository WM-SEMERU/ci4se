def pegasus_elimination_order(n, coordinates=False):
    m = n
    l = 12
    h_order = [4, 5, 6, 7, 0, 1, 2, 3, 8, 9, 10, 11]
    order = []
    for n_i in range(n):
        for l_i in range(0, l, 2):
            for l_v in range(l_i, l_i + 2):
                for m_i in range(m - 1):
                    order.append((0, n_i, l_v, m_i))
            if n_i > 0 and not l_i % 4:
                for m_i in range(m):
                    for l_h in range(h_order[l_i], h_order[l_i] + 4):
                        order.append((1, m_i, l_h, n_i - 1))
    if coordinates:
        return order
    else:
        return pegasus_coordinates(n).ints(order)