def ValidateStopTimesForTrip(self, problems, trip, stop_times):
    prev_departure_secs = -1
    consecutive_stop_times_with_potentially_same_time = 0
    consecutive_stop_times_with_fully_specified_same_time = 0

    def CheckSameTimeCount():
        if (prev_departure_secs != -1 and 
            consecutive_stop_times_with_fully_specified_same_time > 5):
            problems.TooManyConsecutiveStopTimesWithSameTime(trip.trip_id,
                consecutive_stop_times_with_fully_specified_same_time,
                prev_departure_secs)
    for index, st in enumerate(stop_times):
        if st.arrival_secs is None or st.departure_secs is None:
            consecutive_stop_times_with_potentially_same_time += 1
            continue
        if (prev_departure_secs == st.arrival_secs and st.arrival_secs ==
            st.departure_secs):
            consecutive_stop_times_with_potentially_same_time += 1
            consecutive_stop_times_with_fully_specified_same_time = (
                consecutive_stop_times_with_potentially_same_time)
        else:
            CheckSameTimeCount()
            consecutive_stop_times_with_potentially_same_time = 1
            consecutive_stop_times_with_fully_specified_same_time = 1
        prev_departure_secs = st.departure_secs
    CheckSameTimeCount()