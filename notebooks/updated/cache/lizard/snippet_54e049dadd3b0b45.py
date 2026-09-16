def update_record(self, domain, record, data=None, priority=None, ttl=None,
    comment=None):
    rdict = {'id': record.id, 'name': record.name}
    pdict = {'data': data, 'priority': priority, 'ttl': ttl, 'comment': comment
        }
    utils.params_to_dict(pdict, rdict)
    return self.update_records(domain, [rdict])