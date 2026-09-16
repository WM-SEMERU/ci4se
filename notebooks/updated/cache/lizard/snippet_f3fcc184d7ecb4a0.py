def check_the_end_flag(self, state_arr):
    if self.__check_goal_flag(state_arr) is True or self.__check_crash_flag(
        state_arr):
        return True
    else:
        return False