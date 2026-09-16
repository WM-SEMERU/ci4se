def on_ok(self):
    self.parentApp.repo_value['versions'] = {}
    self.parentApp.repo_value['build'] = {}
    for branch in self.branch_cb:
        if self.branch_cb[branch].value:
            self.parentApp.repo_value['versions'][branch] = self.commit_tc[
                branch].values[self.commit_tc[branch].value]
            self.parentApp.repo_value['build'][branch] = True
    if self.error:
        self.quit()
    self.parentApp.addForm('CHOOSETOOLS', ChooseToolsForm, name=
        'Choose tools to add for new plugin\t\t\t\t\t\t^Q to quit', color=
        'CONTROL')
    self.parentApp.change_form('CHOOSETOOLS')