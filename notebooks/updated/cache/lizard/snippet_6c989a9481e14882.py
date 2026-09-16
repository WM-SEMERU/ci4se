def opp_two_point_field_goal_percentage(self):
    try:
        result = float(self.opp_two_point_field_goals) / float(self.
            opp_two_point_field_goal_attempts)
        return round(result, 3)
    except ZeroDivisionError:
        return 0.0