def update_abbreviations(apps, schema_editor):
    Group = apps.get_model('representatives', 'Group')
    amap = {'SenComCult': 'Culture', 'SenComEco': 'Économie', 'SenComDef':
        'Défense', 'SenComEU': 'Europe', 'SenComSoc': 'Social', 'SenComFin':
        'Finances', 'SenComLois': 'Lois', 'SenComDevD': '', 'SenComAppL':
        '', 'AnComCult': 'Culture', 'AnComEco': 'Économie', 'AnComEtrg':
        'Étranger', 'AnComDef': 'Défense', 'AnComEU': 'Europe', 'AnComSoc':
        'Social', 'AnComFin': 'Finances', 'AnComLois': 'Lois', 'AnComDevD':
        '', 'AnComImmu': ''}
    for old, new in amap.iteritems():
        for g in Group.objects.filter(abbreviation=old):
            g.abbreviation = new
            g.save()