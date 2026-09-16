def _sge_get_mem(xmlstring, queue_name):
    rootxml = ET.fromstring(xmlstring)
    my_machine_dict = {}
    rootTag = rootxml.tag.rstrip('qhost')
    for host in rootxml.findall(rootTag + 'host'):
        for queues in host.findall(rootTag + 'queue'):
            if not queue_name or any(q in queues.attrib['name'] for q in
                queue_name.split(',')):
                my_machine_dict[host.attrib['name']] = {}
                for hostvalues in host.findall(rootTag + 'hostvalue'):
                    if 'mem_total' == hostvalues.attrib['name']:
                        if hostvalues.text.lower().endswith('g'):
                            multip = 1
                        elif hostvalues.text.lower().endswith('m'):
                            multip = 1 / float(1024)
                        elif hostvalues.text.lower().endswith('t'):
                            multip = 1024
                        else:
                            raise Exception(
                                'Unrecognized suffix in mem_tot from SGE')
                        my_machine_dict[host.attrib['name']]['mem_total'
                            ] = float(hostvalues.text[:-1]) * float(multip)
                break
    return my_machine_dict