def get_choice_selected_value(self):
    if 'choiceInfo' not in self.dto[self.name]:
        raise GPException('not a choice parameter')
    choice_info_dto = self.dto[self.name]['choiceInfo']
    if 'selectedValue' in choice_info_dto:
        return self.dto[self.name]['choiceInfo']['selectedValue']
    else:
        return None