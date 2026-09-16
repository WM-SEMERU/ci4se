def explode_contact_groups_into_contacts(item, contactgroups):
    if not hasattr(item, 'contact_groups'):
        return
    cgnames = ''
    if item.contact_groups:
        if isinstance(item.contact_groups, list):
            cgnames = item.contact_groups
        else:
            cgnames = item.contact_groups.split(',')
    cgnames = strip_and_uniq(cgnames)
    for cgname in cgnames:
        contactgroup = contactgroups.find_by_name(cgname)
        if not contactgroup:
            item.add_error(
                "The contact group '%s' defined on the %s '%s' do not exist" %
                (cgname, item.__class__.my_type, item.get_name()))
            continue
        cnames = contactgroups.get_members_of_group(cgname)
        if cnames:
            if hasattr(item, 'contacts'):
                item.contacts = item.contacts + cnames
            else:
                item.contacts = cnames