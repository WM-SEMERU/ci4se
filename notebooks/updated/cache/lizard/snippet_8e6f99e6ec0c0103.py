def _post(self, xml_query):
    req = urllib2.Request(url='http://www.rcsb.org/pdb/rest/search', data=
        xml_query)
    f = urllib2.urlopen(req)
    return f.read().strip()