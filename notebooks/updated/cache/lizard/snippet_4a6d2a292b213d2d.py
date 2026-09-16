def debug(self, *debugReqs):
    return self._client.send(debug=sc2api_pb2.RequestDebug(debug=debugReqs))