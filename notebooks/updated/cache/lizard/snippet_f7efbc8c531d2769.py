def get_wide_interims(self):
    outdict = {}
    allowed_states = ['assigned', 'unassigned']
    for analysis in self.context.getAnalyses():
        if api.get_workflow_status_of(analysis) not in allowed_states:
            continue
        if analysis.getKeyword() in outdict.keys():
            continue
        calculation = analysis.getCalculation()
        if not calculation:
            continue
        andict = {'analysis': analysis.Title(), 'keyword': analysis.
            getKeyword(), 'interims': {}}
        for field in analysis.getInterimFields():
            if field.get('wide', False):
                andict['interims'][field['keyword']] = field
        for field in calculation.getInterimFields():
            if field['keyword'] not in andict['interims'].keys() and field.get(
                'wide', False):
                andict['interims'][field['keyword']] = field
        if andict['interims']:
            outdict[analysis.getKeyword()] = andict
    return outdict