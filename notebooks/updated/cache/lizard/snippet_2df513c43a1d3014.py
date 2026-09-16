def OnMouse(self, event):
    node = HotMapNavigator.findNodeAtPosition(self.hot_map, event.GetPosition()
        )
    self.SetHighlight(node, event.GetPosition())