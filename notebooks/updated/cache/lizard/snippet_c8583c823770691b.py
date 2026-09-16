def workspaces(self):
    workspaces = []

    def collect_workspaces(con):
        if con.type == 'workspace' and not con.name.startswith('__'):
            workspaces.append(con)
            return
        for c in con.nodes:
            collect_workspaces(c)
    collect_workspaces(self.root())
    return workspaces