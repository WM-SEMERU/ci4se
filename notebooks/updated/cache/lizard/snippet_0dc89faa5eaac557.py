def GetStartTime(self, problems=problems_module.default_problem_reporter):
    cursor = self._schedule._connection.cursor()
    cursor.execute(
        'SELECT arrival_secs,departure_secs FROM stop_times WHERE trip_id=? ORDER BY stop_sequence LIMIT 1'
        , (self.trip_id,))
    arrival_secs, departure_secs = cursor.fetchone()
    if arrival_secs != None:
        return arrival_secs
    elif departure_secs != None:
        return departure_secs
    else:
        problems.InvalidValue('departure_time', '', 
            'The first stop_time in trip %s is missing times.' % self.trip_id)