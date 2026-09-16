def resolve_by_oai_id(self, oai_id):
    if oai_id.startswith('oai:dnet:'):
        oai_id = oai_id[len('oai:dnet:'):]
    prefix = oai_id.split('::')[0]
    suffix = prefix.replace('_', '').upper()
    oaf = '{0}::{1}'.format(prefix, suffix)
    return self.data.get(oaf)