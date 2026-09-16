def append_instances(cls, inst1, inst2):
    msg = inst1.equal_headers(inst2)
    if msg is not None:
        raise Exception('Cannot appent instances: ' + msg)
    result = cls.copy_instances(inst1)
    for i in xrange(inst2.num_instances):
        result.add_instance(inst2.get_instance(i))
    return result