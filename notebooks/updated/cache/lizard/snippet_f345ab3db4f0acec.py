def get_parameter_tbl(self, parameter):
    par = []
    for entry in parameter.findall('Entry'):
        instance = defaultdict(list)
        instance['Instance'] = entry.find('Instance').text.split()
        if entry.find('ProbTable') is None:
            instance['ValueTable'] = entry.find('ValueTable').text.split()
        else:
            instance['ProbTable'] = entry.find('ProbTable').text.split()
        par.append(instance)
    return par