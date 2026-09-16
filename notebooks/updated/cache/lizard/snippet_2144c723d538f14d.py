def valuefrompostdata(self, postdata):
    if self.id in postdata:
        if isinstance(postdata[self.id], bool) and postdata[self.id
            ] or postdata[self.id] == 1 or postdata[self.id].lower() in ('true'
            , 'yes', 'enabled', '1'):
            return True
        else:
            return False
    else:
        return None