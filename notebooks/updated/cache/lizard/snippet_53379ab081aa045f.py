def remove_workspace(self):

    def confirm_clicked():
        if len(self.document_model.workspaces) > 1:
            command = Workspace.RemoveWorkspaceCommand(self)
            command.perform()
            self.document_controller.push_undo_command(command)
    caption = _("Remove workspace named '{0}'?").format(self.__workspace.name)
    self.pose_confirmation_message_box(caption, confirm_clicked,
        accepted_text=_('Remove Workspace'), message_box_id='remove_workspace')