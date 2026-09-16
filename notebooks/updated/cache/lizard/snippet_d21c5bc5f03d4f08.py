def OnClickRelease(self, event):
    node = HotMapNavigator.findNodeAtPosition(self.hot_map, event.GetPosition()
        )
    self.SetSelected(node, event.GetPosition())