def queue_send(self, frame, callback=None, recv_callback=None):
    frame = self.apply_send_hooks(frame, False)
    self.sendbuf += frame.pack()
    self.sendbuf_frames.append([frame, len(self.sendbuf), callback])
    if recv_callback:
        self.recv_callback = recv_callback