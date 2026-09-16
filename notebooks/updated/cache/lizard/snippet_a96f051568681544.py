def getInvestigators(self, tags=None, seperator=';', _getTag=False):
    if tags is None:
        tags = ['Investigator']
    elif isinstance(tags, str):
        tags = ['Investigator', tags]
    else:
        tags.append('Investigator')
    return super().getInvestigators(tags=tags, seperator=seperator, _getTag
        =_getTag)