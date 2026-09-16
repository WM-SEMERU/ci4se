def oop(aa):
    return ('%s %s %s %.2f %+.2f %s %s %s %s %+.2f %s %s %.2f %.4f %.4f' %
        (aa.stock_no, aa.stock_name, aa.data_date[-1], aa.raw_data[-1], aa.
        range_per, aa.MAC(3), aa.MAC(6), aa.MAC(18), aa.MAO(3, 6)[1], aa.
        MAO(3, 6)[0][1][-1], aa.MAO(3, 6)[0][0], aa.RABC, aa.stock_vol[-1] /
        1000, aa.SD, aa.CV)).encode('utf-8')