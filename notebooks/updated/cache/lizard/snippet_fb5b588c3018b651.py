def sendmany(self, recv_dict, account='', comment=''):
    return self.req('sendmany', [account, recv_dict, comment])