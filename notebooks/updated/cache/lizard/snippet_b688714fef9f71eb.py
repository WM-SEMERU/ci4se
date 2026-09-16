def extract_committees(bill):
    bill_id = bill.get('bill_id', None)
    logger.debug('Extracting Committees for {0}'.format(bill_id))
    committees = bill.get('committees', None)
    committee_map = []
    for c in committees:
        logger.debug('Processing committee {0}'.format(c.get('committee_id')))
        c_list = []
        sub = c.get('subcommittee_id')
        if sub:
            logger.debug('is subcommittee')
            c_list.append('subcommittee')
            c_list.append(c.get('subcommittee'))
            sub_id = '{0}-{1}'.format(c.get('committee_id'), c.get(
                'subcommittee_id'))
            logger.debug('Processing subcommittee {0}'.format(sub_id))
            c_list.append(sub_id)
        else:
            c_list.append('committee')
            c_list.append(c.get('committee'))
            c_list.append(c.get('committee_id'))
        c_list.append(bill_id)
        committee_map.append(c_list)
    return committee_map