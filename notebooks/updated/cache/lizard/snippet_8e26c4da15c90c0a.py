def size_request(self, widget, requisition):
    requisition.width, requisition.height = self.get_desired_size()
    return True