def set_choice_order(self, choice_ids, inline_region):
    reordered_choices = []
    current_choice_ids = [c['id'] for c in self.my_osid_object_form._my_map
        ['choices'][inline_region]]
    if set(choice_ids) != set(current_choice_ids):
        raise IllegalState('missing choices for choice order')
    for choice_id in choice_ids:
        for current_choice in self.my_osid_object_form._my_map['choices'][
            inline_region]:
            if choice_id == current_choice['id']:
                reordered_choices.append(current_choice)
                break
    self.my_osid_object_form._my_map['choices'][inline_region
        ] = reordered_choices