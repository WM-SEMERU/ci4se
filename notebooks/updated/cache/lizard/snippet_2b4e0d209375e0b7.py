def vol(poly1, poly2):
    c_point = central_p(poly1, poly2)
    c_point = c_point[0], c_point[1], c_point[2]
    vol_therah = 0
    num = len(poly1)
    poly1.append(poly1[0])
    poly2.append(poly2[0])
    for i in range(num - 2):
        tehrahedron = [c_point, poly1[0], poly1[i + 1], poly1[i + 2]]
        vol_therah += vol_tehrahedron(tehrahedron)
        tehrahedron = [c_point, poly2[0], poly2[i + 1], poly2[i + 2]]
        vol_therah += vol_tehrahedron(tehrahedron)
    for i in range(num):
        tehrahedron = [c_point, poly1[i], poly2[i], poly2[i + 1]]
        vol_therah += vol_tehrahedron(tehrahedron)
        tehrahedron = [c_point, poly1[i], poly1[i + 1], poly2[i]]
        vol_therah += vol_tehrahedron(tehrahedron)
    return vol_therah