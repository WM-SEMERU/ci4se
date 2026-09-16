def get_groupname(taskfileinfo):
    element = taskfileinfo.task.element
    name = element.name
    return name + '_grp'