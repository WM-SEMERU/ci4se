def inverse_m4x4_transform(mat):
    inv_transform = zeros((4, 4))
    rot = mat[:-1, :-1].T
    inv_transform[:-1, :-1] = rot
    inv_transform[:-1, (-1)] = dot(-rot, mat[:-1, (-1)])
    inv_transform[-1, -1] = 1
    return inv_transform