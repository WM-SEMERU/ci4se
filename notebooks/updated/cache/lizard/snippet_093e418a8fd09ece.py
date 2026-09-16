def add_qtl_to_marker(marker, qtls):
    cnt = 0
    for qtl in qtls:
        if qtl[-1] == marker[0]:
            cnt = cnt + 1
    marker.append(str(cnt))
    return marker