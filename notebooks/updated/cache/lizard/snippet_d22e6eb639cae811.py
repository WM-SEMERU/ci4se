def getReflexRuleElement(self, idx=0, element=''):
    rules_list = self.aq_parent.aq_inner.getReflexRules()
    if len(rules_list) > idx:
        value = rules_list[idx].get(element, '')
        if element == 'actions' and value == '':
            return [{'action': '', 'act_row_idx': '0', 'otherWS': 'current',
                'analyst': '', 'setresulton': '', 'setresultdiscrete': '',
                'worksheettemplate': '', 'setresultvalue': '',
                'an_result_id': ''}]
        elif element == 'conditions' and value == '':
            return [{'analysisservice': '', 'cond_row_idx': '0', 'range0':
                '', 'range1': '', 'discreteresult': '', 'and_or': 'no'}]
        else:
            return value
    if element == 'actions':
        return [{'action': '', 'act_row_idx': '0', 'otherWS': 'current',
            'analyst': '', 'worksheettemplate': '', 'setresulton': '',
            'setresultdiscrete': '', 'setresultvalue': '', 'an_result_id': ''}]
    elif element == 'conditions':
        return [{'analysisservice': '', 'cond_row_idx': '0', 'range0': '',
            'range1': '', 'discreteresult': '', 'and_or': 'no'}]
    else:
        return ''