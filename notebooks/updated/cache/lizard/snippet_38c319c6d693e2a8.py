def chunkWidgets(self, group):
    ui_groups = []
    subgroup = []
    for index, item in enumerate(group['items']):
        if getin(item, ['options', 'full_width'], False):
            ui_groups.append(subgroup)
            ui_groups.append([item])
            subgroup = []
        else:
            subgroup.append(item)
        if len(subgroup) == getin(group, ['options', 'columns'], 2
            ) or item == group['items'][-1]:
            ui_groups.append(subgroup)
            subgroup = []
    return ui_groups