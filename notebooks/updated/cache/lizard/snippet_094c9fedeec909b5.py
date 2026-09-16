def on_open(self, websocket):
    self.pubsub.add_client(ChatClient(websocket, self.channel))