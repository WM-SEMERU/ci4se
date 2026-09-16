def Publish(self, event_name, msg, delay=0):
    events_lib.Events.PublishEvent(event_name, msg, delay=delay)