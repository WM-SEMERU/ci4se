def do_group_by(self, element, decl, pseudo):
    sort_css = groupby_css = flags = ''
    if ',' in decl.value:
        if decl.value.count(',') == 2:
            sort_css, groupby_css, flags = map(serialize, split(decl.value,
                ','))
        else:
            sort_css, groupby_css = map(serialize, split(decl.value, ','))
    else:
        sort_css = serialize(decl.value)
    if groupby_css.strip() == 'nocase':
        flags = groupby_css
        groupby_css = ''
    sort = css_to_func(sort_css, flags, self.css_namespaces, self.state['lang']
        )
    groupby = css_to_func(groupby_css, flags, self.css_namespaces, self.
        state['lang'])
    step = self.state[self.state['current_step']]
    target = self.current_target()
    target.sort = sort
    target.lang = self.state['lang']
    target.isgroup = True
    target.groupby = groupby
    for pos, action in enumerate(reversed(step['actions'])):
        if action[0] == 'target' and action[1].tree == element.etree_element:
            action[1].sort = sort
            action[1].isgroup = True
            action[1].groupby = groupby
            break