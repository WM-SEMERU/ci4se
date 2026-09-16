def solr_to_date(d):
    return '{day}:{m}:{y}'.format(y=d[:4], m=d[5:7], day=d[8:10]) if d else d