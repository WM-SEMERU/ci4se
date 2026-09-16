def ngayThangNam(nn, tt, nnnn, duongLich=True, timeZone=7):
    thangNhuan = 0
    if nn > 0 and nn < 32 and tt < 13 and tt > 0:
        if duongLich is True:
            [nn, tt, nnnn, thangNhuan] = S2L(nn, tt, nnnn, timeZone=timeZone)
        return [nn, tt, nnnn, thangNhuan]
    else:
        raise Exception('Ngày, tháng, năm không chính xác.')