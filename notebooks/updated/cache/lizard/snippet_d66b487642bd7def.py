def on_touch(self, view, event):
    d = self.declaration
    r = {'event': event, 'result': False}
    d.touch_event(r)
    return r['result']