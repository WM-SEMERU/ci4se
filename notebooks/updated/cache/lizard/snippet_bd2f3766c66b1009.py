def pts_change_axis(pts=[], flip=[False, False], offset=[0.0, 0.0]):
    assert isinstance(pts, list) and len(pts) > 0
    l_pt_prev = None
    for pt in pts:
        assert isinstance(pt, tuple)
        l_pt = len(pt)
        assert l_pt > 1
        for i in pt:
            assert isinstance(i, float)
        if l_pt_prev is not None:
            assert l_pt == l_pt_prev
        l_pt_prev = l_pt
    assert isinstance(flip, list)
    l_fl = len(flip)
    assert l_fl == l_pt
    for i in flip:
        assert isinstance(i, bool)
    assert isinstance(offset, list)
    l_of = len(offset)
    assert l_of == l_pt
    for i in offset:
        assert isinstance(i, float)
    return [pt_change_axis(pt, flip, offset) for pt in pts]