def do_sort_by(self, element, decl, pseudo):
    if ',' in decl.value:
        css, flags = split(decl.value, ',')
    else:
        css = decl.value
        flags = None
    sort = css_to_func(serialize(css), serialize(flags or ''), self.
        css_namespaces, self.state['lang'])
    step = self.state[self.state['current_step']]
    target = self.current_target()
    target.sort = sort
    target.lang = self.state['lang']
    target.isgroup = False
    target.groupby = None
    for pos, action in enumerate(reversed(step['actions'])):
        if action[0] == 'target' and action[1].tree == element.etree_element:
            action[1].sort = sort
            action[1].isgroup = False
            action[1].groupby = None
            break