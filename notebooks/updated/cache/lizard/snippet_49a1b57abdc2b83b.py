def locateChild(self, context, segments):
    request = IRequest(context)
    webViewer = IWebViewer(self.store, None)
    childAndSegments = self.siteProduceResource(request, segments, webViewer)
    if childAndSegments is not None:
        return childAndSegments
    return NotFound