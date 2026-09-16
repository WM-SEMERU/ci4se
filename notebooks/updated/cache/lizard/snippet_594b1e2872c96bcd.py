def unregister_project(self, project_node, raise_exception=False):
    if raise_exception:
        if not project_node in self.list_project_nodes():
            raise foundations.exceptions.ProgrammingError(
                "{0} | '{1}' project 'ProjectNode' isn't registered!".
                format(self.__class__.__name__, project_node))
    LOGGER.debug("> Unregistering '{0}' project 'ProjectNode'.".format(
        project_node))
    parent = project_node.parent
    row = project_node.row()
    self.beginRemoveRows(self.get_node_index(parent), row, row)
    parent.remove_child(row)
    self.endRemoveRows()
    self.project_unregistered.emit(project_node)
    return project_node