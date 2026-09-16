def save_replay(self):
    res = self._client.send(save_replay=sc_pb.RequestSaveReplay())
    return res.data