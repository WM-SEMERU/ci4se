def get_time_slice(time, z, zdot=None, timeStart=None, timeEnd=None):
    if timeStart == None:
        timeStart = time[0]
    if timeEnd == None:
        timeEnd = time[-1]
    StartIndex = _np.where(time == take_closest(time, timeStart))[0][0]
    EndIndex = _np.where(time == take_closest(time, timeEnd))[0][0]
    time_sliced = time[StartIndex:EndIndex]
    z_sliced = z[StartIndex:EndIndex]
    if zdot != None:
        zdot_sliced = zdot[StartIndex:EndIndex]
    else:
        zdot_sliced = None
    return time_sliced, z_sliced, zdot_sliced