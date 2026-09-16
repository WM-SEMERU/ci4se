def get_outcome_group(self, group):
    from canvasapi.outcome import OutcomeGroup
    outcome_group_id = obj_or_id(group, 'group', (OutcomeGroup,))
    response = self.__requester.request('GET', 'global/outcome_groups/{}'.
        format(outcome_group_id))
    return OutcomeGroup(self.__requester, response.json())