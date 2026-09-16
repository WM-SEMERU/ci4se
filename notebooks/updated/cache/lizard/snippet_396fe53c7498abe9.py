def find_output(self, ifo, time):
    try:
        lenTime = len(time)
    except TypeError:
        outFile = self.find_output_at_time(ifo, time)
    else:
        if lenTime == 2:
            outFile = self.find_output_in_range(ifo, time[0], time[1])
        if len(time) != 2:
            raise TypeError('I do not understand the input variable time')
    return outFile