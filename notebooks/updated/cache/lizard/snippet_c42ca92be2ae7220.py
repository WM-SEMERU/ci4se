def match_time_series(self, timeseries1, timeseries2):
    time1 = map(lambda item: item[0], timeseries1.to_twodim_list())
    time2 = map(lambda item: item[0], timeseries2.to_twodim_list())
    matches = filter(lambda x: x in time1, time2)
    listX = filter(lambda x: x[0] in matches, timeseries1.to_twodim_list())
    listY = filter(lambda x: x[0] in matches, timeseries2.to_twodim_list())
    return listX, listY