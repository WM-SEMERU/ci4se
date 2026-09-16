def mol3d(self):
    if self._mol3d is None:
        apiurl = (
            'http://www.chemspider.com/MassSpecAPI.asmx/GetRecordMol?csid=%s&calc3d=true&token=%s'
             % (self.csid, TOKEN))
        response = urlopen(apiurl)
        tree = ET.parse(response)
        self._mol3d = tree.getroot().text
    return self._mol3d