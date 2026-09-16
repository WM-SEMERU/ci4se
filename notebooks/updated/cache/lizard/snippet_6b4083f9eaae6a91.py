def writeWarp(self, warpDict):
    warpElement = ET.Element('warp')
    axisNames = sorted(warpDict.keys())
    for name in axisNames:
        axisElement = ET.Element('axis')
        axisElement.attrib['name'] = name
        for a, b in warpDict[name]:
            warpPt = ET.Element('map')
            warpPt.attrib['input'] = str(a)
            warpPt.attrib['output'] = str(b)
            axisElement.append(warpPt)
        warpElement.append(axisElement)
    self.root.append(warpElement)