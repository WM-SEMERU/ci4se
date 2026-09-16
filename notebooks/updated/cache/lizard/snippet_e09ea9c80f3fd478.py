def _createConnectivity(self, linkList, connectList):
    for idx, link in enumerate(linkList):
        connectivity = connectList[idx]
        for upLink in connectivity['upLinks']:
            upstreamLink = UpstreamLink(upstreamLinkID=int(upLink))
            upstreamLink.streamLink = link
        link.downstreamLinkID = int(connectivity['downLink'])
        link.numUpstreamLinks = int(connectivity['numUpLinks'])