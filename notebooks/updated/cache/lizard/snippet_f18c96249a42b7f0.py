def toxml(self):
    chxmlstr = ''
    for event_connection in self.event_connections:
        chxmlstr += event_connection.toxml()
    for for_each in self.for_eachs:
        chxmlstr += for_each.toxml()
    return '<ForEach instances="{0}" as="{1}">{2}</ForEach>'.format(self.
        instances, self.as_, chxmlstr)