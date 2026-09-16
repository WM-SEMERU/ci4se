def getcoords(ddtt):
    n_vertices_index = ddtt.objls.index('Number_of_Vertices')
    first_x = n_vertices_index + 1
    pts = ddtt.obj[first_x:]
    return list(grouper(3, pts))