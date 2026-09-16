def from_qtype_and_id(qtype, queue_id, qname=None):
    for cls in all_subclasses(QueueJob):
        if cls.QTYPE == qtype:
            break
    else:
        logger.critical(
            'Cannot find QueueJob subclass registered for qtype %s' % qtype)
        cls = QueueJob
    return cls(queue_id, qname=qname)