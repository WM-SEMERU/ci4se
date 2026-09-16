def OnSelectReader(self, reader):
    SimpleSCardAppEventObserver.OnSelectReader(self, reader)
    self.feedbacktext.SetLabel('Selected reader: ' + repr(reader))