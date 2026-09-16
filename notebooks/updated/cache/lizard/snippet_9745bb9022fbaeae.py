def extract_possible_actions(self, state_key):
    if state_key in self.__state_action_list_dict:
        return self.__state_action_list_dict[state_key]
    else:
        action_list = []
        state_key_list = [action_list.extend(self.__state_action_list_dict[
            k]) for k in self.__state_action_list_dict.keys() if len([s for
            s in state_key if s in k]) > 0]
        return action_list