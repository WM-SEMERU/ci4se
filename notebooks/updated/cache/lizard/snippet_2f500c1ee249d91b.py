def GetFrequencyStopTimes(self, problems=None):
    stoptimes_list = []
    stoptime_pattern = self.GetStopTimes()
    first_secs = stoptime_pattern[0].arrival_secs
    stoptime_class = self.GetGtfsFactory().StopTime
    for run_secs in self.GetFrequencyStartTimes():
        stoptimes = []
        for st in stoptime_pattern:
            arrival_secs, departure_secs = None, None
            if st.arrival_secs != None:
                arrival_secs = st.arrival_secs - first_secs + run_secs
            if st.departure_secs != None:
                departure_secs = st.departure_secs - first_secs + run_secs
            stoptimes.append(stoptime_class(problems=problems, stop=st.stop,
                arrival_secs=arrival_secs, departure_secs=departure_secs,
                stop_headsign=st.stop_headsign, pickup_type=st.pickup_type,
                drop_off_type=st.drop_off_type, shape_dist_traveled=st.
                shape_dist_traveled, stop_sequence=st.stop_sequence,
                timepoint=st.timepoint))
        stoptimes_list.append(stoptimes)
    return stoptimes_list