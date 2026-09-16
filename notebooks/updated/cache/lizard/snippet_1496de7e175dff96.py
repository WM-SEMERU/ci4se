def to_element(change):
    return tags.Change(tags.Action(change.action), tags.ResourceRecordSet(
        tags.Name(unicode(change.rrset.label)), tags.Type(change.rrset.type
        ), tags.TTL('{}'.format(change.rrset.ttl)), tags.ResourceRecords(
        list(tags.ResourceRecord(tags.Value(rr.to_text())) for rr in sorted
        (change.rrset.records)))))