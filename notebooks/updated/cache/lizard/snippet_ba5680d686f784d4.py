def get_group(self, callb=None):
    if self.group is None:
        mypartial = partial(self.resp_set_group)
        if callb:
            mycallb = lambda x, y: (mypartial(y), callb(x, y))
        else:
            mycallb = lambda x, y: mypartial(y)
        response = self.req_with_resp(GetGroup, StateGroup, callb=callb)
    return self.group