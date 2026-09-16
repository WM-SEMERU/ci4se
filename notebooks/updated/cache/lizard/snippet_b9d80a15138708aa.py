def toxml(self):
    chxmlstr = ''
    for with_ in self.withs:
        chxmlstr += with_.toxml()
    for event_connection in self.event_connections:
        chxmlstr += event_connection.toxml()
    for child_instance in self.child_instances:
        chxmlstr += child_instance.toxml()
    for multi_instantiate in self.multi_instantiates:
        chxmlstr += multi_instantiate.toxml()
    for for_each in self.for_eachs:
        chxmlstr += for_each.toxml()
    if chxmlstr:
        xmlstr = '<Structure>' + chxmlstr + '</Structure>'
    else:
        xmlstr = ''
    return xmlstr