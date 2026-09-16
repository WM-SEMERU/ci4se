def get_chain(self, group_name):
    self.assert_open()
    endgroup = 'Analyses/{}'.format(group_name)
    attr = self.handle[endgroup].attrs
    if 'component' in attr:
        component = attr['component']
    else:
        component = LEGACY_COMPONENT_NAMES[group_name[:-4]]
    chain = deque()
    chain.append((component, group_name))
    groups_to_check = deque()
    groups_to_check.append(endgroup)
    while len(groups_to_check) > 0:
        group = groups_to_check.popleft()
        attr = self.handle[group].attrs
        for key, value in attr.items():
            if str(value).startswith('Analyses/'):
                chain_entry = key, value[9:]
                if chain_entry in chain:
                    chain.remove(chain_entry)
                chain.append(chain_entry)
                groups_to_check.append(value)
    return list(chain)