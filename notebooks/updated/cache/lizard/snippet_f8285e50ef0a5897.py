def find_var_end(self, text):
    return self.find_end(text, self.start_var_token, self.end_var_token)