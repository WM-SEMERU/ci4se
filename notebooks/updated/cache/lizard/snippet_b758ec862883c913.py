def step(self, action):
    obs = None
    reward = None
    info = None
    turn = True
    withturnkey = self.step_options < 2
    withinfo = self.step_options == 0 or self.step_options == 2
    while not self.done and ((obs is None or len(obs) == 0) or withinfo and
        info is None or turn):
        step_message = '<Step' + str(self.step_options
            ) + '>' + self.action_space[action] + '</Step' + str(self.
            step_options) + ' >'
        comms.send_message(self.client_socket, step_message.encode())
        if withturnkey:
            comms.send_message(self.client_socket, self.turn_key.encode())
        obs = comms.recv_message(self.client_socket)
        reply = comms.recv_message(self.client_socket)
        reward, done, sent = struct.unpack('!dbb', reply)
        self.done = done == 1
        if withinfo:
            info = comms.recv_message(self.client_socket).decode('utf-8')
        turn_key = comms.recv_message(self.client_socket).decode('utf-8'
            ) if withturnkey else ''
        if turn_key != '':
            if sent != 0:
                turn = False
            self.turn_key = turn_key
        else:
            turn = sent == 0
        if (obs is None or len(obs) == 0) or turn:
            time.sleep(0.1)
        obs = np.frombuffer(obs, dtype=np.uint8)
    return obs, reward, self.done, info