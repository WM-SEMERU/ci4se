def delete_eventtype(self, test_type_str=None):
    if test_type_str:
        answer = test_type_str, True
    else:
        answer = QInputDialog.getText(self, 'Delete Event Type',
            "Enter event's name to delete")
    if answer[1]:
        self.annot.remove_event_type(answer[0])
        self.display_eventtype()
        self.update_annotations()