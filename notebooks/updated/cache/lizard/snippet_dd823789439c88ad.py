def PLAY(self):
    message = 'PLAY ' + self.session.url + ' RTSP/1.0\r\n'
    message += self.sequence
    message += self.authentication
    message += self.user_agent
    message += self.session_id
    message += '\r\n'
    return message