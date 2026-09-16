def Refresh(self):
    self.dirty = False
    self.data = clc.v2.API.Call('GET', 'groups/%s/%s' % (self.alias, self.
        id), session=self.session)
    self.data['changeInfo']['createdDate'] = clc.v2.time_utils.ZuluTSToSeconds(
        self.data['changeInfo']['createdDate'])
    self.data['changeInfo']['modifiedDate'
        ] = clc.v2.time_utils.ZuluTSToSeconds(self.data['changeInfo'][
        'modifiedDate'])