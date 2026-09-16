def user_return(self, frame, return_value):
    frame.f_locals['__return__'] = return_value
    self.message('--Return--')
    self.interaction(frame, None)