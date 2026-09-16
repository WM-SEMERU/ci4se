def has_magic_children(self):
    if self._child_parts is not None:
        return bool(self._child_parts)
    if self._assessment_section is not None:
        if self.my_osid_object._my_map['maxLevels'
            ] is None or self.my_osid_object._my_map['maxLevels'
            ] > self._level:
            try:
                section = self._assessment_section
                item_id = self.get_my_item_id_from_section(section)
                if not section.is_correct(item_id
                    ) and section.get_confused_learning_objective_ids(item_id
                    ).available() > 0:
                    return True
            except IllegalState:
                pass
    return False